import os
import shutil
from tqdm import tqdm

source_dir = r"D:\codePJ\UIT\CS331\lastterm\OCR-GAN\lib\data\mvtec_anomaly_detection\mvtec_anomaly_detection"
destination_dir = r"D:/codePJ/UIT/CS331/lastterm/OCR-GAN/lib/data/mvtec_anomaly_detection_after"

os.makedirs(destination_dir, exist_ok=True)

for category in tqdm(os.listdir(source_dir), desc="Processing categories"):
    category_path = os.path.join(source_dir, category)

    if os.path.isfile(category_path):
        shutil.copy(category_path, destination_dir)
        continue

    new_category_path = os.path.join(destination_dir, category)
    os.makedirs(new_category_path, exist_ok=True)

    if "test" in os.listdir(category_path):
        for subfolder in tqdm(os.listdir(category_path), desc=f"Processing subfolders in {category}"):
            subfolder_path = os.path.join(category_path, subfolder)
            new_subfolder_path = os.path.join(new_category_path, subfolder)

            if subfolder == "test":
                test_path = os.path.join(category_path, "test")
                new_test_path = os.path.join(new_category_path, "test")
                os.makedirs(new_test_path, exist_ok=True)

                good_dir = os.path.join(new_test_path, "good")
                bad_dir = os.path.join(new_test_path, "bad")
                os.makedirs(good_dir, exist_ok=True)
                os.makedirs(bad_dir, exist_ok=True)

                for test_category in tqdm(os.listdir(test_path), desc=f"Processing test categories in {category}"):
                    test_category_path = os.path.join(test_path, test_category)
                    if not os.path.isdir(test_category_path):
                        continue

                    target_dir = good_dir if test_category == "good" else bad_dir

                    for file_name in os.listdir(test_category_path):
                        src_file = os.path.join(test_category_path, file_name)
                        dest_file = os.path.join(target_dir, file_name)

                        if os.path.exists(dest_file):
                            base, ext = os.path.splitext(file_name)
                            i = 1
                            while os.path.exists(dest_file):
                                dest_file = os.path.join(target_dir, f"{base}_{i}{ext}")
                                i += 1
                        
                        shutil.copy(src_file, dest_file)
            else:
                if os.path.isdir(subfolder_path):
                    shutil.copytree(subfolder_path, new_subfolder_path)
                elif os.path.isfile(subfolder_path):
                    shutil.copy(subfolder_path, new_category_path)
    else:
        if os.path.isdir(category_path):
            shutil.copytree(category_path, new_category_path)

print(f"Dữ liệu đã được xử lý và lưu tại: {destination_dir}")
