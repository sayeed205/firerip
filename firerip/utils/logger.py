class Ytdl_logger:
    file_name = ""

    def debug(self, msg):
        # For compatibility with youtube-dl, both debug and info are passed into debug
        # You can distinguish them by the prefix '[debug] '
        if msg.startswith("[debug] "):
            pass
        else:
            self.info(msg)

    def info(self, msg):
        global file_name
        if "Destination" in msg:
            file_name = (
                msg.split("Destination: ")[1].split(".f")[0].split("\\")[-1]
                + ".mp4"
            )
            # print("file_name: ", file_name)
        if msg.startswith("[download"):
            if "ETA" not in msg:
                if "Destination" not in msg:
                    if "100%" not in msg:
                        print(msg)

            if "ETA" in msg:
                percent = msg.split("%")[0].split(" ")[-1]
                try:
                    percent = float(percent)
                except ValueError:
                    percent = 0
                done_str = "█" * int(float(percent) / 2)
                togo_str = "░" * (50 - int(float(percent) / 2))
                speed = msg.split("at")[1].split("ETA")[0].strip()
                print(
                    (
                        f"Downloading: {file_name} |{done_str}{togo_str}| "
                        + f"{percent}% | {speed}"
                    ),
                    end="\r",
                )
            # pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)
