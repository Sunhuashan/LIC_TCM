ROOT="/root/autodl-tmp/test/"

# DATASET="kodak"
# DATASET="ticnick"
# DATASET="jepgai"
# DATASET="clic21_test"
DATASET="clic_pro_val"
# DATASET="clic22_test"
DATA_PATH="${ROOT}${DATASET}"


python3 eval.py --checkpoint "/root/LIC_TCM/checkpoint/mse_lambda_0.05.pth.tar" \
                --data "$DATA_PATH" --cuda