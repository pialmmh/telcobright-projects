#!/usr/bin/env python3
"""
Deduplicate frames using perceptual hashing.
Groups consecutive similar frames, keeps one representative per group.
Outputs: crm-mightycall/scenes.json with frame groups + timestamp ranges.
"""

import json
from pathlib import Path
import imagehash
from PIL import Image

FRAMES_DIR = Path("crm-mightycall/frames")
OUTPUT_DIR = Path("crm-mightycall")
HASH_THRESHOLD = 8  # hamming distance; lower = stricter (more groups)

frames = sorted(FRAMES_DIR.glob("frame_*.jpg"))
print(f"Total frames: {len(frames)}")

scenes = []
current_group = []
prev_hash = None

for frame in frames:
    idx = int(frame.stem.split("_")[1])
    timestamp = idx - 1  # frame_0001 = second 0

    img = Image.open(frame)
    h = imagehash.phash(img)

    if prev_hash is None or (h - prev_hash) > HASH_THRESHOLD:
        # New scene detected
        if current_group:
            scenes.append(current_group)
        current_group = []

    current_group.append({
        "frame": frame.name,
        "path": str(frame),
        "timestamp": timestamp,
        "timestamp_fmt": f"{timestamp // 60:02d}:{timestamp % 60:02d}"
    })
    prev_hash = h

if current_group:
    scenes.append(current_group)

# Build scene summary: pick middle frame as representative
scene_summaries = []
for i, group in enumerate(scenes):
    mid = group[len(group) // 2]
    scene_summaries.append({
        "scene_index": i,
        "representative_frame": mid["frame"],
        "representative_path": mid["path"],
        "start_time": group[0]["timestamp"],
        "end_time": group[-1]["timestamp"],
        "start_fmt": group[0]["timestamp_fmt"],
        "end_fmt": group[-1]["timestamp_fmt"],
        "duration_sec": group[-1]["timestamp"] - group[0]["timestamp"] + 1,
        "frame_count": len(group),
        "all_frames": [f["frame"] for f in group]
    })

out_path = OUTPUT_DIR / "scenes.json"
with open(out_path, "w") as f:
    json.dump(scene_summaries, f, indent=2)

print(f"Scenes found:  {len(scene_summaries)}")
print(f"Avg duration:  {sum(s['duration_sec'] for s in scene_summaries) / len(scene_summaries):.1f}s per scene")
print(f"Saved to:      {out_path}")
