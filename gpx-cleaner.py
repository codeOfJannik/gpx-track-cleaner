import xml.etree.ElementTree as ET
import os
import sys

def get_gpx_files(directory):
    """
    Creates an array of all gpx files inside a given directory.
    """
    files = []
    for filename in os.listdir(directory):
        if filename.endswith(".gpx"):
            files.append(filename)
    return files

def clear_gpx_track(gpx_file):
    """
    Check all lat/lon values of the trackpoints of a given gpx file.
    If the location data of a trackpoint has not changed compared to the previous trackpoint,
    the trackpoint is removed from the gpx file.
    """
    # Register the custom namespace of gpx files, parse the xml structure and get root element
    ET.register_namespace('', 'http://www.topografix.com/GPX/1/1')
    gpx = ET.parse(gpx_file)
    root = gpx.getroot()
    previous_position = (0.0, 0.0)

    # Iterate over all trackpoints and remove points from gpx where no movement occured
    points = root[1][2].findall('{http://www.topografix.com/GPX/1/1}trkpt')
    for child in points:
        lat = float(child.attrib['lat'])
        lon = float(child.attrib['lon'])
        if lat == previous_position[0] and lon == previous_position[1]:
            root[1][2].remove(child)
        else:
            previous_position = (lat, lon) 
    return gpx


def write_gpx_file(gpx, file):
    """
    Saves the gpx data to the given file location.
    """
    gpx.write(file)  


def main(directory):
    """
    Script for clearing all trackpoints of a gpx file where the lat/lon is not different
    to the previous trackpoint.
    """
    # Check if passed argument is existing directory
    if not os.path.isdir(directory):
        print("Can't find directory ", directory)
        sys.exit(0)

    # Get all gpx files inside the given directory
    gpx_files = get_gpx_files(directory)
    print("Found {} gpx files in directory {}".format(len(gpx_files), directory))

    # Check if output directory exists and create new output dir if not
    output_dir = os.path.join(directory, "output")
    if len(gpx_files) > 0 and not os.path.isdir(output_dir):
        try:
            os.mkdir(output_dir)
        except:
            print("Failed to create output directory")
            sys.exit(1)

    # For each gpx file: clear track points and save new gpx to output dir
    for filename in gpx_files:
        gpx_file = os.path.join(directory, filename)
        cleared_gpx_data = clear_gpx_track(gpx_file)
        write_gpx_file(cleared_gpx_data, os.path.join(output_dir, filename))


if __name__ == "__main__":
    main(sys.argv[1:])