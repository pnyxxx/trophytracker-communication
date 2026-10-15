# TrophyTracker DM — extension Chrome

Sur le **profil ou une publication d'un équipage**, un bouton **✉️ Premier message** en bas à droite lit le nom et le profil de l'équipage et copie un prompt : Claude te rend ton message de présentation de TrophyTracker (ton style, qui dit directement ce que c'est), adapté à l'équipage. Chaque équipage contacté est noté dans le **suivi** (icône de l'extension → Suivi et prompts), où tu coches « A répondu » / « Page créée ».

Sur une **conversation**, un bouton **💬 TrophyTracker DM** ouvre un panneau :

- **📋 Copier les messages** : copie toute la conversation, message par message (`Moi : …` / `Léa : …`).
- **✨ Générer une réponse** : copie un prompt complet (contexte TrophyTracker + conversation + consigne « réponds au dernier message »). Tu le colles dans Claude et tu obtiens le message à envoyer.

Pas d'API, rien de payant, rien n'est envoyé nulle part : l'extension lit seulement ce qui est affiché dans ta page Instagram. Elle n'envoie aucun message à ta place.

## Installer (une fois)

1. Chrome → `chrome://extensions`
2. Active **Mode développeur** (en haut à droite).
3. **Charger l'extension non empaquetée** → choisis ce dossier `extension-copie-dm-instagram`.
4. Recharge l'onglet Instagram s'il était déjà ouvert.

Après une modification des fichiers : bouton ↻ de l'extension dans `chrome://extensions`, puis recharger l'onglet Instagram.

## Utiliser

- « Remonter tout l'historique » (coché) : l'extension fait défiler la conversation vers le haut jusqu'au tout premier message, puis revient en bas. Ne touche pas à la conversation pendant ce temps. Bouton « Arrêter » si c'est trop long.
- Un 2ᵉ clic sur la même conversation est instantané : seuls les nouveaux messages sont ajoutés.
- Le nom de l'interlocuteur est repris de l'en-tête de la conversation ; corrige-le dans le panneau si besoin.

## Modifier les prompts

Clic sur l'icône de l'extension → **Suivi et prompts** → onglet **Prompts** : ton nom, le **contexte du projet** (prix, fonctionnalités, campagne, règles — à mettre à jour quand ça change, ex. le 1er décembre quand le prix repasse à 19 €), la consigne « Premier message » (avec ton message de référence), et la consigne « Générer une réponse ».

Le suivi est stocké dans Chrome, sur cet ordinateur seulement : pense à l'**exporter en CSV** de temps en temps (bouton dans l'onglet Suivi).

Ajouter un bouton plus tard (ex. « Relancer », « Proposer un appel ») : une ligne dans `ACTIONS` en haut de `content.js`, son prompt dans `defaults.js`, et son champ dans `options.html` / `options.js`.

## Si ça ne marche pas

Instagram change régulièrement sa page. Si la copie est vide, incomplète, ou attribue mal les messages : clique sur **Copier un diagnostic (si ça rate)** dans le panneau et colle le résultat à Claude, avec ce qui ne va pas.

Limites connues : dans les réponses à un message (« a répondu à … »), le message cité peut apparaître comme une ligne normale ; les messages vocaux ne sont pas transcrits ; les conversations de groupe ne distinguent pas les différents participants.
