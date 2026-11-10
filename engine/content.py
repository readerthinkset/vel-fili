"""AI phrase generation with permanent no-repeat history."""

from __future__ import annotations

import json
import random
import time
from datetime import datetime

import requests

import config
from config import CATEGORIES, CATEGORIES_NATIVE, HISTORY_DIR, MAX_RECENT_CATEGORIES

PHRASE_HISTORY_FILE = HISTORY_DIR / "all_generated_phrases.json"
RECENT_CATEGORIES_FILE = HISTORY_DIR / "recent_categories.json"

PHRASE_KEY = config.LANGUAGE["history_key"]
LANGUAGE_NAME = config.LANGUAGE["name"]
NATIVE_NAME = config.LANGUAGE["native_name"]

# ==== FALLBACK PHRASES START ====
FALLBACK_PHRASES = [
    {"english": "Hello, nice to meet you.", "native": "Kumusta, ikinagagalak kitang makilala.", "transliteration": "Koo-moo-stah, ee-kee-nah-gah-lahk kee-tahng mah-kee-lah-lah."},
    {"english": "Thank you very much.", "native": "Maraming salamat po.", "transliteration": "Mah-rah-ming sah-lah-maht poh."},
    {"english": "Good morning, have a great day.", "native": "Magandang umaga, magkaroon ka ng magandang araw.", "transliteration": "Mah-gahn-dahng oo-mah-gah, mahg-kah-rohn kah nahng mah-gahn-dahng ah-row."},
    {"english": "I love learning new languages.", "native": "Mahilig akong matuto ng mga bagong wika.", "transliteration": "Mah-hee-leeg ah-kohng mah-too-toh nahng mah-gah bah-gohng wee-kah."},
    {"english": "Never give up on your dreams.", "native": "Huwag na huwag mong isuko ang iyong mga pangarap.", "transliteration": "Hoo-wahg nah hoo-wahg mohng ee-soo-koh ahng ee-yong mah-gah pahng-ah-rahp."},
    {"english": "Every day is a fresh start.", "native": "Bawat araw ay isang bagong simula.", "transliteration": "Bah-waht ah-row ah-ee ee-sahng bah-gohng see-moo-lah."},
    {"english": "Believe in yourself always.", "native": "Manalig ka palagi sa iyong sarili.", "transliteration": "Mah-nah-leeg kah pah-lah-gee sah ee-yong sah-ree-lee."},
    {"english": "Small steps lead to big changes.", "native": "Maliliit na hakbang ang patungo sa malalaking pagbabago.", "transliteration": "Mah-lee-eet nah hahk-bahng ahng pah-too-ngoh sah mah-lah-lah-keeng pahg-bah-goh."},
    {"english": "You are stronger than you think.", "native": "Mas malakas ka kaysa sa iniisip mo.", "transliteration": "Mahs mah-lah-kahs kah kay-sah sah ee-nee-ee-seep moh."},
    {"english": "Happiness is a choice, choose it.", "native": "Ang kaligayahan ay isang pagpili, piliin mo ito.", "transliteration": "Ahng kah-lee-gah-yah-han ah-ee ee-sahng pahg-pee-lee, pee-lee-een moh ee-toh."},
    {"english": "What time is it please.", "native": "Anong oras na po.", "transliteration": "Ah-nohng oh-rahs nah poh."},
    {"english": "Where is the train station.", "native": "Nasaan ang istasyon ng tren.", "transliteration": "Nah-sah-ahn ahng ees-tah-shyon nahng trehn."},
    {"english": "How much does this cost.", "native": "Magkano po ito.", "transliteration": "Mahg-kah-noh poh ee-toh."},
    {"english": "Can you help me please.", "native": "Maaari mo ba akong tulungan.", "transliteration": "Mah-ah-rah-ree moh bah ah-kohng too-loo-ngahn."},
    {"english": "I would like a coffee please.", "native": "Gusto ko ng kape po.", "transliteration": "Goo-stoh koh nahng kah-peh poh."},
    {"english": "The food is delicious today.", "native": "Masarap ang pagkain ngayon.", "transliteration": "Mah-sah-rahp ahng pahg-kah-een nah-goh-yon."},
    {"english": "Have a wonderful weekend.", "native": "Magkaroon ka ng magandang katapusan ng linggo.", "transliteration": "Mahg-kah-rohn kah nahng mah-gahn-dahng kah-tah-poo-sahn nahng leeng-goh."},
    {"english": "Take care of yourself.", "native": "Alagaan mo ang iyong sarili.", "transliteration": "Ah-lah-gah-ahn moh ahng ee-yong sah-ree-lee."},
    {"english": "See you tomorrow my friend.", "native": "Hanggang sa muli, kaibigan.", "transliteration": "Hahng-gahng sah moo-lee, kah-ee-bee-gahn."},
    {"english": "The weather is beautiful outside.", "native": "Maganda ang panahon sa labas.", "transliteration": "Mah-gahn-dah ahng pah-nah-hon sah lah-bahs."},
    {"english": "I am very happy today.", "native": "Masaya ako ngayon.", "transliteration": "Mah-sah-yah ah-koh nah-goh-yon."},
    {"english": "Learning a language opens new doors.", "native": "Ang pag-aaral ng wika ay nagbubukas ng mga bagong pintuan.", "transliteration": "Ahng pahg-ah-rah-ahl nahng wee-kah ah-ee nahg-boo-booh-kahs nahng mah-gah bah-gohng peen-too-ahn."},
    {"english": "Keep practicing every single day.", "native": "Patuloy na magsanay araw-araw.", "transliteration": "Pah-too-looy nah mahg-sah-nahy ah-row-ah-row."},
    {"english": "You can achieve anything you want.", "native": "Kaya mong makamit ang anumang gusto mo.", "transliteration": "Kah-yah mohng mah-kah-meet ahng ah-noo-mahng goo-stoh moh."},
    {"english": "Rest when you are tired.", "native": "Magpahinga kapag pagod ka.", "transliteration": "Mahg-pah-hee-ngah kah-pahg pah-gohd kah."},
    {"english": "Focus on the positive things.", "native": "Mag-pokus sa mga positibong bagay.", "transliteration": "Mahg-poh-koos sah mah-gah poh-see-tee-bohng bah-gay."},
    {"english": "Learn from your mistakes.", "native": "Matuto mula sa iyong mga pagkakamali.", "transliteration": "Mah-too-toh moo-lah sah ee-yong mah-gah pahg-kah-kah-mah-lee."},
    {"english": "Trust the process completely.", "native": "Magtiwala nang lubos sa proseso.", "transliteration": "Mahg-tee-wah-lah nahng loo-boos sah proh-seh-soh."},
    {"english": "Breathe deeply and stay calm.", "native": "Humihinga nang malalim at manatiling kalmado.", "transliteration": "Hoo-mee-hee-ngah nahng mah-lah-leem aht mah-nah-tee-lee-ng kah-lahm-ah-doh."},
    {"english": "Enjoy the little moments in life.", "native": "I-enjoy ang maliliit na sandali sa buhay.", "transliteration": "Ee-en-joy ahng mah-lee-lee-it nah sahn-dah-lee sah boo-hay."},
    {"english": "Smile more, worry less.", "native": "Mas ngumiti, mas kaunti ang pag-aalala.", "transliteration": "Mahs ngoo-mee-tee, mahs kah-oon-tee ahng pahg-ah-lah-lah."},
    {"english": "Be kind to everyone you meet.", "native": "Maging mabait sa lahat ng iyong makikilala.", "transliteration": "Mah-geeng mah-bah-eet sah lah-haht nahng ee-yong mah-kee-kee-lah-lah."},
    {"english": "Help others without expecting anything back.", "native": "Tulungan ang iba nang walang inaasahang kapalit.", "transliteration": "Too-loo-ngahn ahng ee-bah nahng wah-lahng ee-nah-ah-sah-hahng kah-pah-leet."},
    {"english": "Forgive yourself and move forward.", "native": "Patawarin ang iyong sarili at magpatuloy.", "transliteration": "Pah-tah-wah-reen ahng ee-yong sah-ree-lee aht mahg-pah-too-looy."},
    {"english": "Stay strong in difficult times.", "native": "Manatiling matatag sa mahihirap na panahon.", "transliteration": "Mah-nah-tee-lee-ng mah-tah-tahg sah mah-hee-hee-rahp nah pah-nah-hon."},
    {"english": "Every moment is a new beginning.", "native": "Bawat sandali ay isang bagong simula.", "transliteration": "Bah-waht sahn-dah-lee ah-ee ee-sahng bah-gohng see-moo-lah."},
    {"english": "Listen to your heart always.", "native": "Makinig palagi sa iyong puso.", "transliteration": "Mah-kee-neeg pah-lah-gee sah ee-yong poo-soh."},
    {"english": "Do what makes you happy.", "native": "Gawin ang nagpapasaya sa iyo.", "transliteration": "Gah-ween ahng nahg-pah-pah-sah-yah sah ee-yoh."},
    {"english": "Your potential is unlimited.", "native": "Walang hangganan ang iyong potensyal.", "transliteration": "Wah-lahng hahng-gah-nahn ahng ee-yong poh-ten-syal."},
    {"english": "Be brave and take risks.", "native": "Maging matapang at sumubok ng mga panganib.", "transliteration": "Mah-geeng mah-tah-pahng aht soo-bohk nahng mah-gah pahng-ah-neeb."},
    {"english": "Celebrate your progress every day.", "native": "Ipagdiwang ang iyong pag-unlad araw-araw.", "transliteration": "Ee-pahg-dee-wahng ahng ee-yong pahg-oo-nlahd ah-row-ah-row."},
    {"english": "Surround yourself with good people.", "native": "Paligiran ang iyong sarili ng mabubuting tao.", "transliteration": "Pah-lee-gee-rahn ahng ee-yong sah-ree-lee nahng mah-boo-tee-hahnng tah-oh."},
    {"english": "Read books and grow your mind.", "native": "Magbasa ng mga libro at palaguin ang iyong isipan.", "transliteration": "Mahg-bah-sah nahng mah-gah lee-broh aht pah-lah-goo-een ahng ee-yong ee-see-pahn."},
    {"english": "Travel and discover new places.", "native": "Maglakbay at tumuklas ng mga bagong lugar.", "transliteration": "Mahg-lahk-bahy aht too-too-klahs nahng mah-gah bah-gohng loo-gahr."},
    {"english": "Appreciate what you already have.", "native": "Pahalagahan ang mga bagay na mayroon ka na.", "transliteration": "Pah-hah-lah-gah-han ahng mah-gah bah-gay nah mahy-rohn kah nah."},
    {"english": "Dance like nobody is watching.", "native": "Sumayaw na parang walang nanonood.", "transliteration": "Soo-mah-yahw nah pah-rahng wah-lahng nah-nah-noh-ohd."},
    {"english": "Sing from your heart out loud.", "native": "Kumanta mula sa iyong puso nang malakas.", "transliteration": "Koo-mahn-tah moo-lah sah ee-yong poo-soh nahng mah-lah-kahs."},
    {"english": "Plant seeds of kindness everywhere.", "native": "Magtanim ng kabutihan saan man.", "transliteration": "Mahg-tah-neem nahng kah-boo-tee-han sah-ahn mahn."},
    {"english": "Let go of what you cannot control.", "native": "Bitawan ang mga bagay na hindi mo kontrolado.", "transliteration": "Bee-tah-wahn ahng mah-gah bah-gay nah hah-dee moh kohn-troh-lah-doh."},
    {"english": "Be present in the here and now.", "native": "Maging naroroon sa kasalukuyan.", "transliteration": "Mah-geeng nah-rah-roh-ohn sah kah-sah-loo-goo-yahn."},
]
# ==== FALLBACK PHRASES END ====


def _load_json(path, default):
    if path.exists():
        try:
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, OSError):
            pass
    return default


def _save_json(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def load_phrase_history():
    data = _load_json(PHRASE_HISTORY_FILE, {"phrases": [], "last_updated": None})
    data.setdefault("phrases", [])
    return data


def save_phrase_history(data):
    data["last_updated"] = datetime.now().isoformat()
    _save_json(PHRASE_HISTORY_FILE, data)


def is_phrase_used(english):
    english_lower = english.lower().strip()
    for p in load_phrase_history()["phrases"]:
        if p.get("english", "").lower().strip() == english_lower:
            return True
    return False


def _history_native(p):
    for key in (PHRASE_KEY, "vietnamese", "native", "translation", "target"):
        value = p.get(key)
        if value:
            return str(value)
    return ""


def add_phrases_to_history(phrases, category):
    history = load_phrase_history()
    for phrase in phrases:
        history["phrases"].append({
            "english": phrase["english"],
            PHRASE_KEY: phrase["native"],
            "transliteration": phrase.get("transliteration", ""),
            "category": category,
            "generated_at": datetime.now().isoformat(),
        })
    save_phrase_history(history)
    print(f"[content] Saved {len(phrases)} phrases (history total: {len(history['phrases'])})")


def get_available_category():
    data = _load_json(RECENT_CATEGORIES_FILE, {"recent_categories": [], "last_updated": None})
    recent = data.get("recent_categories", [])
    available = [c for c in CATEGORIES if c not in recent]
    if not available:
        recent = recent[-5:]
        available = [c for c in CATEGORIES if c not in recent]
        print("[rotation] Reset recent categories")
    selected = random.choice(available)
    recent.append(selected)
    data["recent_categories"] = recent[-MAX_RECENT_CATEGORIES:]
    data["last_updated"] = datetime.now().isoformat()
    _save_json(RECENT_CATEGORIES_FILE, data)
    print(f"[rotation] Category: {selected} ({len(available)} available)")
    return selected


def _normalize_phrase(item):
    if not isinstance(item, dict):
        return None
    english = str(item.get("english", "")).strip()
    native = str(
        item.get(PHRASE_KEY)
        or item.get("native")
        or item.get("vietnamese")
        or item.get("translation")
        or ""
    ).strip()
    translit = str(item.get("transliteration") or item.get("romanization") or item.get("romaji") or "").strip()
    if not english or not native:
        return None
    if len(english.split()) > 16:
        return None
    if "/" in native or "|" in native:
        native = native.split("/")[0].split("|")[0].strip()
    return {
        "english": english.replace("  ", " ").strip(),
        "native": native.strip(),
        "transliteration": translit.strip().strip("[]"),
    }


def _history_keys(history):
    used_en = set()
    used_nat = set()
    for p in history.get("phrases", []):
        en = str(p.get("english", "")).lower().strip()
        nat = _history_native(p).lower().strip()
        if en:
            used_en.add(en)
        if nat:
            used_nat.add(nat)
    return used_en, used_nat


def generate_phrases(category_english: str, num_phrases: int = 5) -> list:
    category_native = CATEGORIES_NATIVE[category_english]
    history = load_phrase_history()
    used_en, used_nat = _history_keys(history)
    recent_english = [
        p["english"] for p in history["phrases"] if p.get("category") == category_english
    ][-30:]

    models = [config.AI_MODEL]
    if "gemini-fast" not in models:
        models.append("gemini-fast")

    if config.POLLINATIONS_API_KEY:
        for attempt in range(5):
            model = models[0] if attempt < 3 else models[-1]
            try:
                phrases = _request_phrases(category_english, category_native, recent_english, num_phrases, attempt, model)
                unique = []
                for item in phrases:
                    p = _normalize_phrase(item)
                    if not p:
                        continue
                    key_en = p["english"].lower().strip()
                    key_nat = p["native"].lower().strip()
                    if key_en in used_en or key_nat in used_nat:
                        continue
                    if any(key_en == u["english"].lower().strip() for u in unique):
                        continue
                    used_en.add(key_en)
                    used_nat.add(key_nat)
                    unique.append(p)
                    if len(unique) >= num_phrases:
                        break
                if len(unique) >= num_phrases:
                    add_phrases_to_history(unique[:num_phrases], category_english)
                    return unique[:num_phrases]
                print(f"[content] Attempt {attempt + 1}: only {len(unique)} fresh phrases (need {num_phrases})")
            except Exception as exc:  # noqa: BLE001 - network boundary
                print(f"[content] Attempt {attempt + 1} failed ({model}): {exc}")
            time.sleep(1.5 * (attempt + 1))
    else:
        print("[content] No POLLINATIONS_API_KEY, using fallback phrases")

    fresh_fallback = []
    for p in FALLBACK_PHRASES:
        if p["english"].lower().strip() in used_en or p["native"].lower().strip() in used_nat:
            continue
        fresh_fallback.append(p)
    if not fresh_fallback:
        raise RuntimeError("Phrase API unavailable and no unused fallback phrases left; refusing to reuse phrases")
    chosen = fresh_fallback[:num_phrases]
    if len(chosen) < num_phrases:
        print(f"[content] Only {len(chosen)} fresh fallback phrases; building a shorter lesson")
    add_phrases_to_history(chosen, category_english)
    return chosen


def _request_phrases(category_english, category_native, recent_english, num_phrases, attempt, model=None):
    avoid = ""
    if recent_english:
        avoid = "\nDo NOT reuse any of these phrases:\n" + "\n".join(f"- {p}" for p in recent_english)

    prompt = f"""Create {num_phrases * 6} unique {category_english} phrases for English speakers learning {LANGUAGE_NAME}.
{avoid}

Rules:
1. Keep every phrase short and natural (4-11 words in English).
2. Use natural commas for TTS breathing pauses.
3. Each phrase must be speakable in 2-4 seconds.
4. Write clean {LANGUAGE_NAME} in {NATIVE_NAME} with correct accents and orthography. One translation only, no slashes.
5. Transliteration is a friendly Roman-script pronunciation guide for English speakers (not IPA).
6. Vary the sentence patterns and emotions. No duplicates.
7. Phrases must feel like real everyday language, not textbook filler.

Return ONLY a JSON array:
[{{"english": "...", "native": "...", "transliteration": "..."}}]"""

    response = requests.post(
        "https://gen.pollinations.ai/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {config.POLLINATIONS_API_KEY}",
            "Content-Type": "application/json",
        },
        json={
            "model": model or config.AI_MODEL,
            "messages": [
                {"role": "system", "content": f"You are a {LANGUAGE_NAME} teacher creating short, natural, varied bilingual phrases. Reply with JSON only."},
                {"role": "user", "content": prompt},
            ],
            "temperature": min(0.95 + attempt * 0.02, 1.0),
        },
        timeout=90,
    )
    response.raise_for_status()
    content = response.json()["choices"][0]["message"]["content"].strip()

    if "```json" in content:
        content = content.split("```json", 1)[1].split("```", 1)[0].strip()
    elif "```" in content:
        content = content.split("```", 1)[1].split("```", 1)[0].strip()

    start = content.find("[")
    end = content.rfind("]")
    if start >= 0 and end > start:
        content = content[start:end + 1]

    data = json.loads(content)
    if not isinstance(data, list):
        raise ValueError("AI did not return a JSON array")
    return data
