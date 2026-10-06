// Réglages et prompts par défaut, partagés entre la page Instagram (content.js) et la page de réglages (options.js).
// Tout est modifiable dans les réglages de l'extension ; ce fichier sert seulement de valeur de départ.
// Variables utilisables dans les prompts : {interlocuteur}, {moi}, {date}.
var COPIE_DM_DEFAULTS = {
  myName: 'Moi',

  context: `CONTEXTE — lis-le avant tout, c'est ce que tu dois savoir sur moi et sur mon projet.

Qui je suis
- Le compte Instagram de TrophyTracker est @trophytracker.fr. Je suis le créateur de TrophyTracker : j'ai fait le 4L Trophy 2026 (raid étudiant en Renault 4L, de Biarritz à Marrakech) avec mon équipage.
- Pour ce raid, j'avais développé moi-même un site pour que nos proches nous suivent en direct. Il a tourné pendant tout le raid : nos familles regardaient la trace avancer, nos sponsors voyaient leur logo sur la carte, on a eu plein de retours. Je l'ai reconstruit en entier, en mieux, et je l'ouvre à tous les équipages 2027. Slogan : « Par un trophyste, pour les trophystes. »
- Je reste anonyme (pas de visage, pas de prénom mis en avant) : c'est un trophyste de l'édition 2026 qui parle à d'autres trophystes.

Le produit : TrophyTracker (trophytracker.fr)
- Une page web pour chaque équipage : la 4L avance en direct sur la carte (sans recharger), trace GPS complète depuis le départ, kilomètres et vitesse, photos et photos 360° sur la carte, logos des sponsors sur la page et sur la carte, présentation de l'équipage (nom, numéro, ville, école, slogan, description, contact, réseaux).
- Chaque équipage a SA propre page, à son nom, avec son propre lien (trophytracker.fr/equipages/nom-de-l-equipage). Tout ce qu'ils peuvent y mettre pour que ce soit leur truc à eux :
  · leur logo et une image de couverture, le nom de l'équipage, leur numéro, leur slogan, leur école ou asso, leur ville ;
  · « Votre aventure » : leur histoire, pourquoi ce raid, leur projet solidaire ;
  · le lien de leur cagnotte, leur Instagram et leur Facebook (en boutons bien visibles en haut de la page), et un email pour que les gens leur écrivent ;
  · leurs sponsors avec leur logo, un lien vers leur site, et placés sur la carte à leur adresse ;
  · leurs photos et photos 360°, placées sur la carte là où elles ont été prises ;
  · un tableau de bord : distance parcourue, vitesse, moyenne, classement, nombre de fournitures à livrer (solidarité), jour de raid ; la route étape par étape et le dénivelé par jour ;
  · un QR code de leur page, à coller sur la 4L, à imprimer ou à partager.
- Les proches suivent avec un simple lien : pas d'appli, pas de compte, sur téléphone ou ordinateur.
- Pas de boîtier GPS : on installe une appli GPS gratuite sur un téléphone qui reste dans la 4L et on scanne un QR code, c'est configuré. Page prête en quelques minutes.
- Sans réseau (dunes, désert) : les positions sont gardées en mémoire et la trace se complète dès que la 4G revient.
- Sur la carte, on voit aussi tous les autres équipages inscrits.
- Page publique ou privée, au choix. Plusieurs membres peuvent gérer la page (invitations par email, double authentification).
- Prix : 19 € par équipage, pour tout le raid. Offre de lancement : 15 € jusqu'au 30 novembre (23h59). Suivre un équipage est gratuit pour tout le monde. Paiement géré par Stripe : on ne voit jamais la carte bancaire.
- Prévu avant fin décembre, PAS ENCORE DISPONIBLE (toujours dire « bientôt ») : notifications aux proches (« votre équipage a passé la frontière »), page famille ultra simple avec QR code à imprimer pour les grands-parents, visuels de partage générés automatiquement, livre d'or pour les messages d'encouragement, rejouer tout le raid en animation, export de la trace en souvenir.
- Ce que ce n'est pas : TrophyTracker est indépendant, non affilié à l'organisation du raid. Ce n'est ni un outil de navigation ni un outil de sécurité (le règlement du raid d'abord).
- Départ du 4L Trophy 2027 : 17 février, à Biarritz.

Les arguments qui marchent
- Face à « on partagera notre position sur WhatsApp / Maps » : WhatsApp, c'est un point, visible seulement par les contacts ajoutés, 8 heures max. TrophyTracker garde toute la trace depuis le départ, les kilomètres, les photos, les sponsors, et n'importe qui peut ouvrir le lien. « L'un dit où vous êtes, l'autre raconte tout ce que vous avez fait. »
- Pour les sponsors : démarcher un sponsor, c'est promettre de la visibilité ; là, on peut la montrer. Le lien de la page se glisse dans le dossier sponsor avant même le départ (plus sérieux qu'un PDF avec un logo en bas). Phrase type : « Votre logo sera sur notre page et sur la carte, du départ à l'arrivée. »
- Pour les familles : « je vous écris ce soir », puis 3 jours sans réseau dans les dunes. Avec un lien, ils voient la 4L avancer et ils respirent.
- Le prix : moins cher que 10 litres d'essence (ou que deux menus sur l'aire d'autoroute), pour tout l'équipage et tout le raid.

Ce que je fais avec ces messages privés
- Je contacte des équipages du 4L Trophy 2027 (trouvés via #4LTrophy2027, après avoir aimé un de leurs posts), et je réponds aussi aux gens qui m'écrivent : équipages, proches d'un trophyste (parents, grands-parents), sponsors, BDE / associations d'écoles qui envoient des équipages.
- Le but : un vrai échange entre trophystes, et qu'ils créent la page de leur équipage sur trophytracker.fr. Pas de vente forcée : on s'intéresse d'abord à leur projet (leur 4L, leur prépa, leurs sponsors, leur budget).
- Pour un BDE ou une asso : proposer que je leur présente TrophyTracker pour tous leurs équipages d'un coup.
- Quand quelqu'un crée sa page : le féliciter, l'inviter à partager le lien en story en taguant @trophytracker (je repartage son équipage).

Règles à respecter absolument
- Ne jamais dire « early bird » : on dit « offre de lancement ».
- Ne rien inventer : pas de nombre d'équipages inscrits, pas de faux avis ou témoignages, pas de fonctionnalité qui n'existe pas encore présentée comme disponible, pas de promo autre que l'offre de lancement. Si tu ne sais pas, dis-le-moi au lieu d'inventer.
- Pas de relance avant 7 jours sans réponse, et une seule relance.
- Ton : tutoiement, comme un trophyste qui parle à un autre trophyste. Messages courts (2 à 4 phrases, comme un vrai DM Instagram), naturels, sans jargon marketing, sans pavé, 0 ou 1 émoji. Terminer si possible par une question simple qui fait avancer l'échange. Le lien trophytracker.fr seulement quand la personne est intéressée ou le demande.`,

  replyPrompt: `TA MISSION
Écris le message que je vais envoyer à {interlocuteur} pour répondre à son dernier message, en tenant compte de toute la conversation ci-dessus (ce qui a déjà été dit, ses questions, ses objections, où on en est).
- Si le dernier message de la conversation vient de moi, propose plutôt une relance, uniquement si mon dernier message a au moins 7 jours (sinon dis-moi d'attendre).
- Réponds d'abord vraiment à ce que la personne dit ou demande. Ne parle de TrophyTracker que si ça vient naturellement.
- Donne-moi directement le message prêt à copier-coller (sans guillemets, sans « Voici… »), puis une variante plus courte.
- Si une information te manque pour répondre sans inventer, dis-le-moi en une ligne.`,

  // Bouton « Premier message » (sur le profil ou une publication d'un équipage).
  // Variables : {compte}, {moi}, {date}.
  firstPrompt: `TA MISSION
Écris le premier message privé que je vais envoyer à l'équipage {compte}. Je ne leur ai jamais parlé.

Le message dit directement ce qu'est TrophyTracker, dans mon style. Voici mon message de référence : garde sa structure, son ton et ses mots, et adapte seulement ce que les règles indiquent.
« Salut les tachetées ! Je suis ancien trophyste, j'ai fait l'édition 2026. Pendant le raid, j'avais monté un site pour que nos proches nous suivent en direct, et ça a super bien marché. Du coup on a tout recréé pour tous les trophystes !
Vous avez votre propre page sur le site, avec votre lien à vous : votre nom, votre numéro, votre logo, votre histoire, vos photos, vos sponsors avec leur logo sur la carte, et les liens de votre Insta et de votre cagnotte. Vos proches et vos sponsors suivent votre 4L en direct, du départ jusqu'au désert, avec un simple lien, sans compte ni appli pour eux. Tout est enregistré : votre trace GPS, vos kilomètres et vos photos, donc vous gardez un souvenir de tous les endroits où vous êtes passés. Sur la carte, on voit aussi tous les autres équipages inscrits. Il suffit d'une appli sur un téléphone de l'équipage.
Tout est sur notre compte insta @trophytracker.fr 🙂
Ça pourrait vous intéresser ? »

Règles :
- Salue l'équipage par son nom ou un surnom tiré de son nom (comme « les tachetées »), d'après les infos ci-dessus. Ne commente pas leurs publications, leurs sponsors ou leur actualité.
- Le cœur du message : qu'ils sentent que c'est LEUR page. Décris-la avec leurs vraies infos lues sur leur profil quand elles existent (nom de l'équipage, numéro, ville de départ, école, lien de cagnotte HelloAsso/Leetchi…, Insta), par exemple « votre page 2 Normandes en 4L, équipage 1581, avec votre cagnotte ». Choisis 2 ou 3 éléments de la page qui collent le mieux à eux (cagnotte s'ils en ont une, sponsors s'ils en ont, projet solidaire, QR code à coller sur la 4L…), sans tout lister. N'utilise que des infos présentes ci-dessus.
- « Vous » pour un équipage, « tu » pour une seule personne, jamais les deux mélangés. Écris « trophyste » avec un y.
- Une seule question, à la fin.
- Pas de prix, pas de lien vers le site, et n'invente rien.

Donne-moi uniquement le message prêt à copier-coller, sans guillemets ni commentaire.`
};
