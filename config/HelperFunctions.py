from PIL import Image, ImageDraw
import codecs
import  os, csv, sys

def readPath(folder_path):
    if os.path.exists(folder_path):
        files = os.listdir(folder_path)
        language_data = {}

        for f in files:
            file_data = {}
            file_path = os.path.join(folder_path, f)
            file_name = f.strip('.csv')

            with codecs.open(file_path, encoding='utf-32') as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                line_count = 0

                temp_data = []

                for row in csv_reader:
                    # Add Labels
                    if line_count == 0:
                        line_count += 1
                        file_data['labels'] = row

                    # Add Data
                    else:
                        temp_data.append([ repr(row[0]), repr(row[1]) ])
                file_data['characters'] = temp_data

            language_data[file_name] = file_data
        return language_data

    else:
        print("Error")
        sys.exit()


def displayLangObject(input_object):
    keys = []
    print("-----------------------------------------------------------------")
    for key in input_object:
        keys.append(key)
        print('*', key)

        for sub_key in input_object[key]:
            print(' -- ' + sub_key + ', (' + str(len(input_object[key][sub_key])) + ')' )
    print("-----------------------------------------------------------------")


def getTextDimensions(text_string, font):
    ascent, descent = font.getmetrics()
    text_width = font.getmask(text_string).getbbox()[2]
    text_height = font.getmask(text_string).getbbox()[3] + descent
    return (text_width, text_height)