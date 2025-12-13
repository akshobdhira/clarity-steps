try:
    import google.adk
    print("Found google.adk")
    import google.adk.runner
    print("Found google.adk.runner")
except ImportError as e:
    print(f"ImportError: {e}")
except Exception as e:
    print(f"Error: {e}")
