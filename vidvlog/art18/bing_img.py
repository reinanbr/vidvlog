from bing_image_downloader import downloader

print(downloader.download("Natasha Nice", limit=5,  output_dir='dataset', adult_filter_off=False, force_replace=False, timeout=60, verbose=True))
