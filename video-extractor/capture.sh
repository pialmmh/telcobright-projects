#!/bin/bash
# Screen capture: 1fps for 480 seconds (8 minutes)
OUT="/home/mustafa/telcobright-projects/video-extractor/crm-mightycall/frames"
mkdir -p "$OUT"
echo "Capturing started at $(date)" | tee "$OUT/../capture.log"
ffmpeg -f x11grab -r 1 -s 1920x1080 -i :0.0 -t 480 -q:v 2 "$OUT/frame_%04d.jpg" -y 2>>"$OUT/../capture.log"
echo "Capture done at $(date). Frames: $(ls $OUT/frame_*.jpg 2>/dev/null | wc -l)" | tee -a "$OUT/../capture.log"
