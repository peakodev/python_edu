import os
import shutil
from concurrent.futures import ThreadPoolExecutor, as_completed
import argparse
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(threadName)s : %(message)s')


def copy_file(file_path, destination_dir) -> None:
    """
    Copies a file to the specified destination directory based on its extension.
    """
    try:
        if not os.path.exists(destination_dir):
            os.makedirs(destination_dir)

        base_name = os.path.basename(file_path)
        destination_path = os.path.join(destination_dir, base_name)

        # Handle the case where the file already exists
        if os.path.exists(destination_path):
            base, ext = os.path.splitext(base_name)
            counter = 1
            while os.path.exists(destination_path):
                new_base_name = f"{base}_{counter}{ext}"
                destination_path = os.path.join(destination_dir, new_base_name)
                counter += 1

        shutil.copy(file_path, destination_path)
        logging.info(f"Copied file {file_path} to {destination_path}")
    except Exception as e:
        logging.error(f"Error copying file {file_path} to {destination_dir}: {e}")


def process_directory(directory, base_output_dir) -> None:
    """
    Processes a directory: sorts files by extension and copies them to corresponding directories.
    """
    with ThreadPoolExecutor(max_workers=os.cpu_count()) as executor:
        futures = []
        for root, dirs, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                file_extension = file.split('.')[-1]
                destination_dir = os.path.join(base_output_dir, file_extension)
                futures.append(executor.submit(copy_file, file_path, destination_dir))

            # Process subdirectories in separate threads
            for dir in dirs:
                sub_dir_path = os.path.join(root, dir)
                futures.append(executor.submit(process_directory, sub_dir_path, base_output_dir))

        for future in as_completed(futures):
            try:
                future.result()
            except Exception as e:
                logging.error(f"Error in processing directory {directory}: {e}")


def main(junk_folder, output_folder) -> None:
    """
    Main function to start the processing of the "Junk" folder.
    """
    if not os.path.exists(junk_folder):
        logging.error(f"The folder {junk_folder} does not exist.")
        return

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    logging.info(f"Starting processing of folder {junk_folder}")
    process_directory(junk_folder, output_folder)
    logging.info(f"Completed processing of folder {junk_folder}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Sort files in the Junk folder by extensions using multiple threads.")
    parser.add_argument("junk_folder",
                        type=str,
                        help="Path to the junk folder to be processed.")
    parser.add_argument("output_folder",
                        type=str,
                        help="Path to the output folder where sorted files will be stored.")

    args = parser.parse_args()
    junk_folder = args.junk_folder
    output_folder = args.output_folder

    main(junk_folder, output_folder)
