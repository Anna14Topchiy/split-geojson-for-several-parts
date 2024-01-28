import geopandas as gpd
import os

def split_geojson(input_file, output_directory, num_files=10):
    gdf = gpd.read_file(input_file)

    total_records = len(gdf)
    records_per_file = total_records // num_files
    remainder = total_records % num_files

    file_name, file_extension = os.path.splitext(os.path.basename(input_file))

    for i in range(num_files):
        start_index = i * records_per_file
        end_index = start_index + records_per_file

        if i < remainder:
            end_index += 1

        output_file = os.path.join(output_directory, f'{file_name}_{i+1}{file_extension}')
        gdf.iloc[start_index:end_index].to_file(output_file, driver='GeoJSON')

if __name__ == "__main__":
    input_geojson_file = r'C:\Users\annat\OneDrive\kasko\source_preparation_for_each_country\NL\scrip_snap_points_to_line\mly_map_feature_traffic_sign_stop_14_8346_8503_5448_5411.geojson'  # Замените на путь к вашему GeoJSON файлу
    output_directory = r'C:\\Users\\annat\\OneDrive\\kasko\\source_preparation_for_each_country\\NL\\scrip_snap_points_to_line'  # Замените на папку, куда вы хотите сохранить маленькие файлы
    num_files = 10  # Количество файлов, на которые нужно разбить

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    split_geojson(input_geojson_file, output_directory, num_files)
