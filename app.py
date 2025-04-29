import base64
import binascii # To catch base64 decoding errors
import codecs   # To handle potential unicode errors after decoding
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# --- Configuration ---
# Replace with your ACTUAL Printify store URL
PRINTIFY_STORE_URL = "https://your-printify-store-url.com"
# Or, if you have a specific Printify Pop-Up store link:
# PRINTIFY_STORE_URL = "https://your-popup-store.printify.com/products"

# --- Routes ---

@app.route('/')
def home():
    """
    Handles the landing page.
    Checks for a 'msg' query parameter, decodes it from base64,
    and passes it to the template.
    """
    encoded_message = request.args.get('msg')
    decoded_message = None
    error_message = None

    if encoded_message:
        try:
            # Decode base64
            decoded_bytes = base64.b64decode(encoded_message)
            # Decode bytes to string (handle potential errors)
            decoded_message = codecs.decode(decoded_bytes, 'utf-8', 'ignore')
        except (binascii.Error, UnicodeDecodeError):
            # Handle cases where the input is not valid base64 or doesn't decode to UTF-8
            error_message = "Invalid message format."
        except Exception as e:
            # Catch any other unexpected errors during decoding
            print(f"Error decoding message: {e}") # Log the error for debugging
            error_message = "Could not display the message."

        # If there was an error, override the decoded_message
        if error_message:
            decoded_message = error_message


    return render_template('index.html', message=decoded_message)

@app.route('/shop')
def shop():
    """
    Serves the shop page, which links to the external Printify store.
    """
    # Option 1: Render a simple page with a link
    return render_template('shop.html', printify_url=PRINTIFY_STORE_URL)

    # Option 2: Directly redirect to the Printify store (less flexible)
    # return redirect(PRINTIFY_STORE_URL)

# --- Run Application ---
if __name__ == '__main__':
    # Set debug=False for production
    app.run(debug=False)
