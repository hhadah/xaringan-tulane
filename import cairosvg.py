import cairosvg

def convert_eps_to_svg(eps_path, svg_path):
    # Convert EPS to SVG
    cairosvg.eps2svg(url=eps_path, write_to=svg_path)

# Usage example:
convert_eps_to_svg("/Users/hhadah/Documents/GiT/xaringan-tulane/assets/UHLogo-black.eps", "/Users/hhadah/Documents/GiT/xaringan-tulane/assets/UHLogo-black.svg")
convert_eps_to_svg("/Users/hhadah/Documents/GiT/xaringan-tulane/assets/UHLogo-white.eps", "/Users/hhadah/Documents/GiT/xaringan-tulane/assets/UHLogo-white.svg")
convert_eps_to_svg("/Users/hhadah/Documents/GiT/xaringan-tulane/assets/UHLogo.eps", "/Users/hhadah/Documents/GiT/xaringan-tulane/assets/UHLogo.svg")
