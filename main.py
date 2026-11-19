"""
This runner copies 'entry.png' to the directory specified by the MAKEFUN_OUTPUT_DIR
environment variable, or to '/output' if not set. The copy is byte-identical.
This script uses only the Python 3 standard library.
"""
import os
import shutil
import sys

def main():
    source = "entry.png"
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    
    # Ensure source exists in the current directory
    if not os.path.exists(source):
        # Try to find it relative to the script if not in CWD
        script_dir = os.path.dirname(os.path.abspath(__file__))
        source = os.path.join(script_dir, "entry.png")
        if not os.path.exists(source):
            print(f"Error: entry.png not found.", file=sys.stderr)
            sys.exit(1)
            
    # Ensure output directory exists
    if not os.path.exists(output_dir):
        try:
            os.makedirs(output_dir, exist_ok=True)
        except Exception:
            # If we can't create it, we'll likely fail the copy anyway
            pass

    target = os.path.join(output_dir, "entry.png")
    
    try:
        source_size = os.path.getsize(source)
        shutil.copyfile(source, target)
        target_size = os.path.getsize(target)
        
        if source_size != target_size:
            print(f"Error: size mismatch! Source: {source_size}, Target: {target_size}", file=sys.stderr)
            sys.exit(1)
            
        print(f"copied {target_size} bytes", file=sys.stderr)
        print(target)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
