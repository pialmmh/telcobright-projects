#!/bin/bash
# Screen capture of a single window at 1fps.
# Usage: ./capture-window.sh <folder-name> <duration-seconds>
# Focus the target window (e.g. Chrome with the video) BEFORE running this.
# After it starts, you can switch to other windows — capture region is fixed
# at the focused window's position/size at start. Don't move/resize the
# target window during capture.

set -e
NAME="${1:-capture}"
DURATION="${2:-300}"
OUT="/home/mustafa/telcobright-projects/video-extractor/${NAME}/frames"

WIN=$(xdotool getactivewindow)
TITLE=$(xdotool getwindowname "$WIN")
eval $(xdotool getwindowgeometry --shell "$WIN")
# Vars set: WINDOW, X, Y, WIDTH, HEIGHT, SCREEN

# x11grab requires even width/height
W=$(( WIDTH - WIDTH % 2 ))
H=$(( HEIGHT - HEIGHT % 2 ))

mkdir -p "$OUT"
LOG="${OUT}/../capture.log"
{
  echo "Capturing window '${TITLE}' (id=${WIN})"
  echo "Region: ${W}x${H} at +${X},${Y}"
  echo "Folder: ${NAME}, duration: ${DURATION}s, started: $(date)"
} | tee "$LOG"

ffmpeg -f x11grab -r 1 -s "${W}x${H}" -i ":0.0+${X},${Y}" \
       -t "$DURATION" -q:v 2 "$OUT/frame_%04d.jpg" -y 2>>"$LOG"

echo "Capture done at $(date). Frames: $(ls $OUT/frame_*.jpg 2>/dev/null | wc -l)" | tee -a "$LOG"
