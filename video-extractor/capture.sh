#!/bin/bash
# Screen capture at 1fps
# Usage: ./capture.sh <folder-name> <duration-seconds>
# Example: ./capture.sh preview-dialer 378

NAME="${1:-capture}"
DURATION="${2:-300}"
OUT="/home/mustafa/telcobright-projects/video-extractor/${NAME}/frames"

mkdir -p "$OUT"
echo "Capturing '${NAME}' for ${DURATION}s, started at $(date)" | tee "${OUT}/../capture.log"
ffmpeg -f x11grab -r 1 -s 1920x1080 -i :0.0 -t "$DURATION" -q:v 2 "$OUT/frame_%04d.jpg" -y 2>>"${OUT}/../capture.log"
echo "Capture done at $(date). Frames: $(ls $OUT/frame_*.jpg 2>/dev/null | wc -l)" | tee -a "${OUT}/../capture.log"
