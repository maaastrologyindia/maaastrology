import zipfile, os, re, json, shutil
from PIL import Image
from pathlib import Path

root=Path('/mnt/data/maa_final')
prodroot=root/'public'/'products'
prodzip='/mnt/data/Bracelets.zip'
products=[
('pyrite','Pyrite Bracelet','Wealth & Abundance'),
('love-attracting','Love Attracting Bracelet','Love & Harmony'),
('citrine','Citrine Bracelet','Confidence & Prosperity'),
('tiger-eye','Tiger Eye Bracelet','Courage & Focus'),
('lapis-lazuli','Lapis Lazuli Bracelet','Wisdom & Expression'),
('green-aventurine','Green Aventurine Bracelet','Growth & Opportunity'),
('amethyst','Amethyst Bracelet','Calm & Clarity'),
('black-obsidian','Black Obsidian Bracelet','Grounding & Protection'),
('moonstone','Moonstone Bracelet','Intuition & Balance'),
('labradorite','Labradorite Bracelet','Transformation & Intuition'),
]
folder_map={name:slug for slug,name,_ in products}

with zipfile.ZipFile(prodzip) as z:
    for folder,slug in folder_map.items():
        files=[n for n in z.namelist() if n.startswith('Bracelets/'+folder+'/') and n.lower().endswith('.png')]
        out=prodroot/slug; out.mkdir(parents=True,exist_ok=True)
        for i,n in enumerate(files,1):
            data=z.read(n)
            im=Image.open(__import__('io').BytesIO(data)).convert('RGB')
            # Main/gallery web image: max 900px tall, quality 82
            if im.height>1200:
                ratio=1200/im.height; im=im.resize((round(im.width*ratio),1200),Image.LANCZOS)
            im.save(out/f'{i}.webp','WEBP',quality=82,method=6)
            # thumbnail
            thumb=im.copy(); thumb.thumbnail((220,300),Image.LANCZOS)
            thumb.save(out/f'{i}-thumb.webp','WEBP',quality=76,method=6)

# product json
pdata=[]
for slug,name,tag in products:
    benefits={
      'pyrite':['Abundance symbolism','Confidence & ambition','A premium everyday statement'],
      'love-attracting':['Love & harmony symbolism','Heart-centred intention','Elegant everyday wear'],
      'citrine':['Prosperity symbolism','Positive intention','Warm, uplifting style'],
      'tiger-eye':['Courage symbolism','Focus & determination','Classic earthy finish'],
      'lapis-lazuli':['Wisdom symbolism','Expression & confidence','Rich blue gemstone look'],
      'green-aventurine':['Growth symbolism','Opportunity & optimism','Fresh green gemstone look'],
      'amethyst':['Calm symbolism','Mindful intention','Elegant purple gemstone look'],
      'black-obsidian':['Grounding symbolism','Protective intention','Minimal black gemstone look'],
      'moonstone':['Intuition symbolism','Balance & reflection','Soft luminous gemstone look'],
      'labradorite':['Transformation symbolism','Intuition & curiosity','Natural iridescent character'],
    }[slug]
    pdata.append({'id':slug,'name':name,'price':399,'tag':tag,'images':[f'/products/{slug}/{i}.webp' for i in range(1,6)],'benefits':benefits,'description':f'{name} from Maa Astrology is presented as a premium gemstone accessory for personal intention, mindfulness and everyday style. Traditional gemstone symbolism varies by belief and practice; it is not a guarantee of a particular result.'})
(root/'data'/'products.json').write_text(json.dumps(pdata,indent=2,ensure_ascii=False))
