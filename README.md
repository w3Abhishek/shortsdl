# shortsdl

**shortsdl** is a Python package for downloading videos from popular short video platforms such as TikTok, Instagram, Chingari, Josh, Moj, Triller, ShareChat, Mitron, Roposo, and LitLot.

## Features

- **Multi-Platform Support:** Download videos from a variety of short video platforms.
- **Command Line Interface (CLI):** Easily download videos directly from your terminal.
- **Python API:** Integrate video downloading capabilities into your Python projects.
- **Modular Design:** Extend or add new platform support with minimal effort.

## Installation

You can install **shortsdl** using pip:

```bash
pip install shortsdl
```

## Usage

### Command Line

To download a video from the command line, simply provide the video URL and (optionally) an output file name:

```bash
shortsdl <video_url> -o <output_file>
```

For example:

```bash
shortsdl https://www.tiktok.com/@example/video/1234567890 -o myvideo.mp4
```

### Python API

You can also use **shortsdl** directly in your Python code:

```python
from shortsdl import download_video

# Download video and save to 'video.mp4'
download_video("https://www.tiktok.com/@example/video/1234567890", output="video.mp4")
```

## File Structure

The package is structured in a modular way to support multiple platforms:

```
shortsdl/
├── __init__.py
├── cli.py
├── downloader.py
├── utils.py
├── platforms
│   ├── __init__.py
│   ├── base.py
│   ├── tiktok.py
│   ├── instagram.py
│   ├── chingari.py
│   ├── josh.py
│   ├── moj.py
│   ├── triller.py
│   ├── sharechat.py
│   ├── mitron.py
│   ├── roposo.py
│   └── litlot.py
├── setup.py
├── pyproject.toml
├── README.md
├── LICENSE
└── requirements.txt
```

Each platform-specific module implements a downloader class that extends a base class, ensuring consistency and ease of maintenance.

## Contributing

Contributions are welcome! If you have ideas or improvements, please consider:

- Opening an issue to discuss your ideas.
- Forking the repository and submitting a pull request.
- Writing tests and documentation for new features.

Before contributing, please review our [Contribution Guidelines](CONTRIBUTING.md) (if available).

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or suggestions, please open an issue in our GitHub repository or contact the maintainer directly.

---

Happy downloading!