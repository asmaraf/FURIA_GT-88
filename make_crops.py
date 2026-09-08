import os
# pyrefly: ignore [missing-import]
from PIL import Image

os.makedirs("assets/crops", exist_ok=True)

# 1. Hero image crops
hero = Image.open("assets/hero.jpeg")
hw, hh = hero.size

# crop-origin.webp: Centered dramatic crop of the wedge front 16:9
# hero is 1376 x 768
origin = hero.crop((int(hw * 0.1), int(hh * 0.15), int(hw * 0.85), int(hh * 0.95)))
origin.save("assets/crops/crop-origin.webp", "WEBP", quality=88)

# 2. Craft 01: Slatted louvers crop from Ch1 frame (frame_0045.webp)
f_louvers = Image.open("frames/frame_0045.webp")
lw, lh = f_louvers.size
# Crop tight on the black slatted engine cover
crop_louvers = f_louvers.crop((int(lw * 0.1), int(lh * 0.15), int(lw * 0.9), int(lh * 0.95)))
crop_louvers.save("assets/crops/crop-louvers.webp", "WEBP", quality=88)

# 3. Craft 02: Pop-up lights crop from Ch4 frame (frame_0280.webp)
f_lights = Image.open("frames/frame_0280.webp")
fw, fh = f_lights.size
crop_lights = f_lights.crop((int(fw * 0.12), int(fh * 0.2), int(fw * 0.88), int(fh * 0.85)))
crop_lights.save("assets/crops/crop-lights.webp", "WEBP", quality=88)

# 4. Gallery items
# g1 (4/3 aspect ratio): Rear wing and deck
f_wing = Image.open("frames/frame_0210.webp")
ww, wh = f_wing.size
g1 = f_wing.crop((int(ww * 0.05), int(wh * 0.1), int(ww * 0.95), int(wh * 0.9)))
g1 = g1.resize((1000, 750), Image.Resampling.LANCZOS)
g1.save("assets/crops/gallery-1.webp", "WEBP", quality=88)

# g2 (4/5 aspect ratio): Pop-up headlight detail portrait
g2 = f_lights.crop((int(fw * 0.1), int(fh * 0.25), int(fw * 0.55), int(fh * 0.85)))
g2 = g2.resize((800, 1000), Image.Resampling.LANCZOS)
g2.save("assets/crops/gallery-2.webp", "WEBP", quality=88)

# g3 (1/1 square aspect ratio): Disassembled chassis / wheel detail
f_assembly = Image.open("frames/frame_0110.webp")
aw, ah = f_assembly.size
g3 = f_assembly.crop((int(aw * 0.45), int(ah * 0.3), int(aw * 0.95), int(ah * 0.9)))
g3 = g3.resize((800, 800), Image.Resampling.LANCZOS)
g3.save("assets/crops/gallery-3.webp", "WEBP", quality=88)

# g4 (16/10 aspect ratio): Hero beauty three-quarters stance
f_hero = Image.open("frames/frame_0385.webp")
bw, bh = f_hero.size
g4 = f_hero.crop((int(bw * 0.1), int(bh * 0.18), int(bw * 0.9), int(bh * 0.88)))
g4 = g4.resize((1120, 700), Image.Resampling.LANCZOS)
g4.save("assets/crops/gallery-4.webp", "WEBP", quality=88)

print("Crops generated successfully:")
for f in os.listdir("assets/crops"):
    p = os.path.join("assets/crops", f)
    print(f"  {f}: {os.path.getsize(p)} bytes")
