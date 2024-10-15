CUDA_VISIBLE_DEVICES='0' python -u ./train.py -d /root/autodl-tmp/ \
    --cuda --N 128 --lambda 0.05 --epochs 50 --lr_epoch 45 48 \
    --save_path /root/LIC_TCM/checkpoint/ --save 