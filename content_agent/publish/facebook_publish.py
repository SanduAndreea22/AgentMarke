#!/usr/bin/env python3
"""Publică o postare Facebook generată de content_agent, prin Meta Graph API.

Nu publică niciodată automat, fără intervenție umană — citește un fișier
deja aprobat din content_agent/outputs/facebook/, arată exact ce urmează
să publice, și cere confirmare explicită (da/nu) înainte de orice apel
către API. --dry-run arată totul fără să trimită nimic.

Uz:
    python content_agent/publish/facebook_publish.py content_agent/outputs/facebook/2026-09-08-ceva.md
    python content_agent/publish/facebook_publish.py content_agent/outputs/facebook/2026-09-08-ceva.md --image poza.jpg
    python content_agent/publish/facebook_publish.py content_agent/outputs/facebook/2026-09-08-ceva.md --dry-run

Setup necesar: vezi content_agent/publish/README.md.
"""

import argparse
import os
import re
import sys
from pathlib import Path

import requests

try:
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    pass

GRAPH_API_VERSION = "v21.0"


def extract_section(content, heading):
    pattern = rf"## {re.escape(heading)}\n\n(.*?)(?:\n\n## |\Z)"
    match = re.search(pattern, content, re.DOTALL)
    return match.group(1).strip() if match else None


def build_message(content):
    postare = extract_section(content, "Postare")
    if not postare:
        raise ValueError("Nu am găsit secțiunea '## Postare' în fișier.")
    hashtags = extract_section(content, "Hashtag-uri")
    if hashtags and hashtags != "—":
        return f"{postare}\n\n{hashtags}"
    return postare


def extract_planted_comment(content):
    inchidere = extract_section(content, "Închidere")
    if not inchidere:
        return None
    match = re.search(r"\*\*Comentariu plantat[^*]*\*\*:?\s*(.+)", inchidere)
    return match.group(1).strip() if match else None


def publish_text_post(page_id, access_token, message, dry_run):
    url = f"https://graph.facebook.com/{GRAPH_API_VERSION}/{page_id}/feed"
    if dry_run:
        print("[DRY RUN] Nu s-a trimis nimic — ar fi mers la:", url)
        return {"id": "DRY_RUN_FAKE_ID"}
    response = requests.post(url, data={"message": message, "access_token": access_token})
    response.raise_for_status()
    return response.json()


def publish_photo_post(page_id, access_token, message, image_path, dry_run):
    url = f"https://graph.facebook.com/{GRAPH_API_VERSION}/{page_id}/photos"
    if dry_run:
        print("[DRY RUN] Nu s-a trimis nimic — ar fi mers la:", url, "cu imaginea", image_path)
        return {"id": "DRY_RUN_FAKE_ID"}
    with open(image_path, "rb") as image_file:
        response = requests.post(
            url,
            data={"caption": message, "access_token": access_token},
            files={"source": image_file},
        )
    response.raise_for_status()
    return response.json()


def publish_comment(post_id, access_token, comment_text, dry_run):
    url = f"https://graph.facebook.com/{GRAPH_API_VERSION}/{post_id}/comments"
    if dry_run:
        print("[DRY RUN] Comentariul plantat nu a fost trimis — ar fi fost:")
        print(comment_text)
        return
    response = requests.post(url, data={"message": comment_text, "access_token": access_token})
    response.raise_for_status()


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("post_file", help="Fișierul .md din content_agent/outputs/facebook/")
    parser.add_argument("--image", help="Cale locală către imaginea de atașat (opțional)")
    parser.add_argument("--dry-run", action="store_true", help="Arată ce s-ar publica, fără să trimită nimic")
    parser.add_argument(
        "--yes",
        action="store_true",
        help="Sări peste promptul interactiv de confirmare — folosește doar când Andreea a confirmat deja "
        "explicit, în conversație, exact acest fișier (ex. când Claude rulează scriptul pentru ea).",
    )
    args = parser.parse_args()

    post_path = Path(args.post_file)
    if not post_path.exists():
        print(f"Fișierul nu există: {post_path}")
        sys.exit(1)

    page_id = os.environ.get("FACEBOOK_PAGE_ID")
    access_token = os.environ.get("FACEBOOK_PAGE_ACCESS_TOKEN")

    if not args.dry_run and (not page_id or not access_token):
        print("Lipsesc FACEBOOK_PAGE_ID sau FACEBOOK_PAGE_ACCESS_TOKEN din mediu/.env.")
        print("Vezi content_agent/publish/README.md pentru setup, sau rulează cu --dry-run.")
        sys.exit(1)

    content = post_path.read_text(encoding="utf-8")
    message = build_message(content)
    planted_comment = extract_planted_comment(content)

    print(f"--- Postare de publicat ({post_path.name}) ---\n")
    print(message)
    if args.image:
        print(f"\n[Imagine atașată: {args.image}]")
    if planted_comment:
        print(f"\n[Comentariu plantat, se adaugă automat imediat după]: {planted_comment}")
    print("\n---")

    if args.yes:
        print("\n(Confirmare preluată din conversație, cu --yes — nu se mai cere din nou aici.)")
    else:
        confirm = input("\nConfirmi publicarea? (scrie exact 'da' pentru a continua): ").strip().lower()
        if confirm != "da":
            print("Anulat — nimic nu a fost publicat.")
            sys.exit(0)

    if args.image:
        result = publish_photo_post(page_id, access_token, message, args.image, args.dry_run)
    else:
        result = publish_text_post(page_id, access_token, message, args.dry_run)

    print("Publicat:", result)

    if planted_comment and result.get("id"):
        publish_comment(result["id"], access_token, planted_comment, args.dry_run)
        print("Comentariu plantat adăugat.")


if __name__ == "__main__":
    main()
