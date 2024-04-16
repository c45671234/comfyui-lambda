import os
os.system(f"git lfs install")
os.system(f"git clone https://github.com/comfyanonymous/ComfyUI /home/ubuntu/ui/ComfyUI")
os.chdir(f"/home/ubuntu/ui/ComfyUI")
os.system(f"pip install -r requirements.txt")
os.system(f"git clone https://github.com/ltdrdata/ComfyUI-Manager /home/demo/source/ComfyUI/custom_nodes/ComfyUI-Manager")
os.system(f"python main.py --port 8266 --enable-cors-header")
