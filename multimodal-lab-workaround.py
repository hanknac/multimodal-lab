# If you see the error, "multimodal embedding failed with the following error deadline",
# when generating embeddings for image or video, use the following workaround in the 
# notebook to create image embeddings and video embeddings


# Image Embedding cell 1 - copy the image locally
!gsutil cp gs://github-repo/embeddings/getting_started_embeddings/gms_images/GGOEACBA104999.jpg .

# Image Embedding cell 2 - generate the image embeddings
image_path = "./GGOEACBA104999.jpg"
image_emb = get_image_embedding(image_path=image_path)

print("length of embedding: ", len(image_emb))
print("First five values are: ", image_emb[:5])

# Video embedding cell 1 - copy the video locally
!gsutil cp gs://github-repo/embeddings/getting_started_embeddings/UCF-101-subset/BrushingTeeth/v_BrushingTeeth_g01_c02.mp4 .

# Video embedding cell 2 - generate the video embeddings
video_path = "./v_BrushingTeeth_g01_c02.mp4"
video_emb = get_video_embedding(
    video_path=video_path,
)

print("length of embedding: ", len(video_emb[0]))
print("First five values of the first segment are: ", video_emb[0][:5])