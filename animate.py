import streamlit as st
import moviepy.editor as mpy
from PIL import Image
import numpy as np
import requests
from io import BytesIO

def generate_image(prompt):
    """
    Dummy function to generate an image based on a prompt.
    You can integrate DALL·E or another AI image generator here.
    """
    st.write(f"Generating image for: {prompt}")
    # Placeholder: Use a default image
    img_url = "https://via.placeholder.com/512"
    response = requests.get(img_url)
    img = Image.open(BytesIO(response.content))
    return img

def create_video(animal, bird):
    """
    Generate an animated video based on the given animal and bird names.
    """
    st.write("Creating animation...")
    
    # Generate images
    img1 = generate_image(f"A {animal} in a forest")
    img2 = generate_image(f"A {bird} flying in the sky")
    
    # Convert to numpy arrays
    img1 = np.array(img1)
    img2 = np.array(img2)
    
    # Create a simple animation (fade transition)
    clip1 = mpy.ImageSequenceClip([img1, img2], fps=1)
    
    # Save video
    video_path = "animated_video.mp4"
    clip1.write_videofile(video_path, codec="libx264", fps=1)
    return video_path

def main():
    st.title("Animal & Bird Animation Generator")
    
    animal = st.text_input("Enter an animal name", "Lion")
    bird = st.text_input("Enter a bird name", "Eagle")
    
    if st.button("Generate Video"):
        video_path = create_video(animal, bird)
        st.video(video_path)
        
        with open(video_path, "rb") as file:
            st.download_button("Download Video", file, file_name="animation.mp4", mime="video/mp4")

if __name__ == "__main__":
    main()
