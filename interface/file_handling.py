import pandas as pd


def format_filename(s):
    """
    https://gist.github.com/seanh/93666
    Take a string and return a valid filename constructed from the string.
    Uses a whitelist approach: any characters not present in valid_chars are
    removed. Also spaces are replaced with underscores.
    
    Note: this method may produce invalid filenames such as ``, `.` or `..`
    When I use this method I prepend a date string like '2009_01_15_19_46_32_'
    and append a file extension like '.txt', so I avoid the potential of using
    an invalid filename.
    """
    valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
    filename = ''.join(c for c in s if c in valid_chars)
    filename = filename.replace(' ', '_')  # I don't like spaces in filenames.
    return filename


def export_recorded(filename, plot_d):
    channel_names, data_channels= plot_d
    N = len(channel_names) # number of pins
    n = len(data_channels[0])
    pass


def import_recorded(filename):
    frame = pd.read_table(filename, ';', dtype=str)
    channel_names = list()
    data_channels = list()
    for i in frame.columns:
        channel_names.append(i)
        data_channels.append(frame[str(i)].astype(int).tolist())
    return [channel_names, data_channels]
