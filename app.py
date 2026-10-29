
import streamlit as st

from crypto_utils import encrypt_file, decrypt_file

st.set_page_config(
    page_title="SecureVault",
    page_icon="🔐",
    layout="centered",
)

st.title("🔐 SecureVault")
st.caption("Secure File Encryption and Decryption System")

st.info(
    "Protect your files using password-derived AES-256-GCM encryption."
)

mode = st.radio(
    "Choose an operation",
    ["Encrypt File", "Decrypt File"],
    horizontal=True,
)

uploaded_file = st.file_uploader(
    "Choose a file",
    key=mode,
)

password = st.text_input(
    "Encryption password",
    type="password",
    help="Use a strong password. Keep it safe; it cannot be recovered.",
)

if mode == "Encrypt File":
    st.write("The selected file will be encrypted before download.")

    if st.button("Encrypt File", type="primary"):
        if uploaded_file is None:
            st.error("Please select a file first.")
        elif len(password) < 12:
            st.error("Use a password of at least 12 characters.")
        else:
            try:
                encrypted_data = encrypt_file(
                    uploaded_file.getvalue(),
                    password,
                )

                output_name = uploaded_file.name + ".enc"

                st.success("Encryption completed successfully.")

                st.download_button(
                    "Download Encrypted File",
                    data=encrypted_data,
                    file_name=output_name,
                    mime="application/octet-stream",
                )

            except Exception:
                st.error("Encryption failed. Please try again.")

else:
    st.write("Upload a .enc file created by SecureVault.")

    if st.button("Decrypt File", type="primary"):
        if uploaded_file is None:
            st.error("Please select an encrypted file first.")
        elif len(password) == 0:
            st.error("Please enter your password.")
        else:
            try:
                encrypted_data = uploaded_file.getvalue()

                decrypted_data = decrypt_file(
                    encrypted_data,
                    password,
                )

                original_name = uploaded_file.name

                if original_name.endswith(".enc"):
                    original_name = original_name[:-4]
                else:
                    original_name = "decrypted_file"

                st.success("Decryption and authentication successful.")

                st.download_button(
                    "Download Decrypted File",
                    data=decrypted_data,
                    file_name=original_name,
                    mime="application/octet-stream",
                )

            except ValueError as error:
                st.error(str(error))
            except Exception:
                st.error("Decryption failed. Check the file and try again.")

st.divider()
st.caption(
    "Educational cybersecurity project. "
    "Always keep a secure backup of your original files."
)
