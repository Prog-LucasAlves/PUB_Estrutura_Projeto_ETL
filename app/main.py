from pipeline.extract import extract_from_excel
from pipeline.transform import concat_data_frames
from pipeline.load import load_excel

if __name__ == "__main__":
    data_frame_list = extract_from_excel("../data/input")
    data_frame = concat_data_frames(data_frame_list)
    load_excel(data_frame, "../data/output", "output")
