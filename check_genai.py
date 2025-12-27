try:
    import google.generativeai as genai
    print("Found google.generativeai")
except ImportError:
    print("Missing google.generativeai")
