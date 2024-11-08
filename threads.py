# from threadspipepy import threadspipe
from threadspipepy.threadspipe import ThreadsPipe

import os

from dotenv import load_dotenv

load_dotenv()

# https://github.com/settings/tokens?type=beta


api = ThreadsPipe(
    access_token=os.environ['long_lived_access_token'], 
    user_id=os.environ['user_id'], 
    handle_hashtags=True, 
    auto_handle_hashtags=False, 
    gh_bearer_token = os.environ['f_grain_token'],
    gh_repo_name = 'threads-files',
    gh_username = 'paulosabayomi',
)

# 500
xpost_text_1 = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc ultrices, ante in feugiat pharetra, lectus nunc tincidunt nibh, in efficitur sapien massa nec dolor. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Sed euismod, nisi vel semper ultricies, augue velit blandit odio, et ultrices ante quam id orci. Donec euismod, erat non tincidunt aliquet, velit dui ultrices lorem, quis malesuada sapien diam a nunc. Sed et velit vitae arcu luctus ornare."

xpost_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc ultrices, ante in feugiat pharetra, lectus nunc tincidunt nibh, in efficitur sapien massa nec dolor. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Sed euismod, nisi vel semper ultricies, augue velit blandit odio, et ultrices ante quam id orci. Donec euismod, erat non tincidunt aliquet, velit dui ultrices lorem, quis malesuada sapien diam a nunc. Sed et velit vitae arcu luctus ornare. \
        \
        Maecenas placerat, quam id aliquet volutpat, odio nisi lacinia nisl, quis scelerisque enim felis non ipsum. Duis et nulla sit amet elit aliquam aliquet. Nulla facilisi. Sed a lacus et quam elementum pulvinar. Sed sed sapien et nunc tempus lacinia. Nulla facilisi. Nulla facilisi. Mauris viverra lacinia mauris, quis blandit enim ultricies vel. \
            \
        Nulla facilisi. Suspendisse venenatis, urna sit amet rhoncus dignissim, nisl nunc pharetra est, sit amet auctor eros nunc id mi. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Donec pellentesque, tellus et feugiat porttitor, sapien ante sollicitudin sapien, vitae aliquet erat mauris quis ipsum.\
            \
        Nulla facilisi. Maecenas id massa sed odio vulputate dignissim. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Mauris non ipsum sed ante elementum aliquet. Maecenas id massa sed odio vulputate dignissim. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Sed et velit vitae arcu luctus ornare.\
            \
        Nulla facilisi. Sed et velit vitae arcu luctus ornare. Sed et velit vitae arcu luctus ornare. Nulla facilisi. Sed et velit vitae arcu luctus ornare. Nulla facilisi. Sed et velit vitae arcu luctus ornare. Nulla facilisi. Sed et velit vitae arcu luctus ornare. Nulla facilisi. Sed et velit vitae arcu luctus ornare. Nulla facilisi. Sed et velit vitae arcu luctus ornare. Nulla facilisi. Sed et velit vitae arcu luctus ornare. Nulla facilisi. Sed et velit vitae arcu luctus ornare. Nulla facilisi. Sed et velit vitae arcu luctus ornare. Nulla facilisi. Sed et velit vitae arcu luctus ornare. Nulla facilisi. Sed et velit vitae arcu luctus ornare. Nulla facilisi. Sed et velit vitae arcu luctus ornare. Nulla facilisi. Sed et velit vitae arcu luctus ornare. Nulla facilisi. Sed et velit vitae arcu luctus ornare. Nulla facilisi. Sed et velit vitae arcu luctus ornare. Nulla facilisi. Sed et velit vitae arcu luctus ornare. Nulla facilisi. Sed et velit vitae arcu luctus ornare. Nulla facilisi. Sed et velit vitae arcu luctus ornare. Nulla facilisi. Sed et velit vitae arcu luctus ornare. Nulla facilisi. Sed et velit vitae arcu luctus ornare. Nulla facilisi. Sed et velit vitae arcu luctus ornare. Nulla facilisi. Sed et velit vitae arcu luctus ornare. Nulla facilisi. Sed et velit vitae arcu luctus ornare. Nulla facilisi. Sed et velit vitae arcu luctus ornare. Nulla facilisi. Sed et velit vitae arcu luctus ornare. Nulla facilisi. Sed et velit vitae arcu luctus ornare. Nulla facilisi. Sed et velit vitae arcu luctus ornare. Nulla facilisi. Sed et velit vitae arcu luctus ornare. Nulla facilisi. Sed et velit vitae arcu luctus ornare. Nulla facilisi. Sed et velit vitae arcu luctus ornare. Nulla facilisi. Sed et velit vitae arcu luctus ornare. Nulla facilisi. Sed et velit vitae arcu luctus ornare. Nulla facilisi. Sed et velit vitae arcu luctus ornare. Nulla facilisi. Sed et velit vitae arcu luctus ornare. Nulla facilisi. Sed et velit vitae arcu luctus ornare. Nulla facilisi. Sed et velit vitae arcu luctus ornare. Nulla facilisi. Sed et velit vitae arcu luctus ornare. Nulla facilisi. Sed et velit vitae arcu luctus ornare. Nulla facilisi. Sed et velit vitae arcu luctus ornare. Nulla facilisi. Sed et velit vitae arcu luctus ornare. Nulla facilisi. Sed et velit vitae arcu luctus ornare. Nulla facilisi. Sed et velit vitae arcu luctus ornare. Nulla facilisi. Sed et velit vitae arcu luctus ornare. Nulla facilisi. Sed et velit vitae arcu luctus ornare. Nulla facilisi. Sed et velit vitae arcu luctus ornare. Nulla facilisi. Sed et velit vitae arcu luctus ornare. Nulla facilisi. Sed et velit vitae arcu luctus ornare. Nulla facilisi. Sed et velit vitae arcu luctus ornare. Nulla facilisi. Sed et velit vitae arcu luctus ornare. Nulla facilisi. Sed et velit vitae arcu luctus ornare. Nulla facilisi. Sed et velit vitae arcu luctus ornare. Nulla facilisi. Sed et velit vitae arcu luctus ornare. Nulla facilisi. Sed et velit vitae arcu luctus ornare. Nulla facilisi. Sed et velit vitae arcu luctus ornare. Nulla facilisi. Sed et velit vitae arcu luctus ornare. Nulla facilisi. Sed et velit vitae arcu luctus ornare. Nulla facilisi. Sed et velit vitae arcu luctus ornare. Nulla facilisi. Sed et velit vitae arcu luctus ornare. Nulla facilisi. Sed et velit vitae arcu luctus ornare. Nulla facilisi. Sed et velit vitae arcu luctus ornare. Nulla facilisi. Sed et velit vitae arcu luctus ornare. Nulla facilisi. Sed et velit vitae arcu luctus ornare. Nulla facilisi. Sed et velit vitae arcu luctus ornare. Nulla facilisi. Sed et velit vitae arcu luctus ornare. Nulla facilisi. Sed et velit vitae arcu luctus ornare. Nulla facilisi. Sed et velit vitae arcu luctus ornare. Nulla facilisi. Sed et velit vitae arcu luctus ornare. Nulla facilisi. Sed et velit vitae arcu luctus ornare. Nulla facilisi. Sed et velit vitae arcu luctus ornare. Nulla facilisi. Sed et velit vitae arcu luctus ornare. Nulla facilisi. Sed et velit vitae arcu luctus ornare. Nulla facilisi. Sed et velit vitae arcu luctus ornare. Nulla facilisi. Sed et velit vitae arcu luctus ornare. Nulla facilisi. Sed et velit vitae arcu luctus ornare. Nulla facilisi. Sed et velit vitae arcu luctus ornare. Nulla facilisi. Sed et velit vitae arcu luctus ornare. Nulla facilisi. Sed et velit vitae arcu luctus ornare. Nulla facilisi. Sed et velit vitae arcu luctus ornare. Nulla facilisi. Sed et velit vitae arcu luctus ornare. Nulla facilisi. Sed et velit vitae arcu luctus ornare. Nulla facilisi. Sed et velit vitae arcu luctus ornare. Nulla facilisi. Sed et velit vitae arcu luctus ornare. Nulla facilisi. Sed et velit vitae arcu luctus ornare. Nulla facilisi. Sed et velit vitae arcu luctus ornare. Nulla facilisi. Sed et velit vitae arcu luctus ornare. Nulla facilisi. Sed et velit vitae arcu luctus ornare. Nulla facilisi. Sed et velit vitae arcu luctus ornare. Nulla facilisi. Sed et velit vitae arcu luctus ornare. Nulla facilisi. Sed et velit vitae arcu luctus ornare. Nulla facilisi. Sed et velit vitae arcu luctus ornare. Nulla facilisi. Sed et velit vitae arcu luctus ornare. Nulla facilisi. Sed et velit vitae arcu luctus ornare. Nulla facilisi. Sed et vel"

pipe = api.pipe(
    xpost_text,
    files=[
        "https://images.unsplash.com/photo-1504639725590-34d0984388bd?q=80&w=2574&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        # open('sample-5.mp4', 'rb').read(),
        "https://images.unsplash.com/photo-1721332149371-fa99da451baa?q=80&w=2536&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDF8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        "https://images.unsplash.com/photo-1725554515068-8bb766ba0724?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxmZWF0dXJlZC1waG90b3MtZmVlZHwxMnx8fGVufDB8fHx8fA%3D%3D",
        "./img-2.jpg",
        "https://images.unsplash.com/photo-1725647093138-e1ef909ca53c?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxmZWF0dXJlZC1waG90b3MtZmVlZHwxNnx8fGVufDB8fHx8fA%3D%3D",
        "https://images.unsplash.com/photo-1725489890999-84e4f2f71327?q=80&w=2574&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        "https://images.unsplash.com/photo-1725829879131-1780c5291059?q=80&w=2574&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        "https://images.unsplash.com/photo-1725628736546-6b334a2002d7?q=80&w=2574&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        "https://images.unsplash.com/photo-1725714355497-a4da39972ef2?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxmZWF0dXJlZC1waG90b3MtZmVlZHwzMnx8fGVufDB8fHx8fA%3D%3D",
        "https://images.unsplash.com/photo-1725792630033-e462b10672ec?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxmZWF0dXJlZC1waG90b3MtZmVlZHwzNnx8fGVufDB8fHx8fA%3D%3D",
        "https://images.unsplash.com/photo-1724764147620-598dd5356fd7?q=80&w=2574&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        "https://images.unsplash.com/photo-1725462567088-0898ef927c8d?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxmZWF0dXJlZC1waG90b3MtZmVlZHw0MHx8fGVufDB8fHx8fA%3D%3D",
        "https://images.unsplash.com/photo-1726809755769-cc8cb426b57b?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxmZWF0dXJlZC1waG90b3MtZmVlZHw0fHx8ZW58MHx8fHx8",
        "https://images.unsplash.com/photo-1726510114046-b7938cdc1bd1?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxmZWF0dXJlZC1waG90b3MtZmVlZHw1fHx8ZW58MHx8fHx8",
        "https://images.unsplash.com/photo-1726533870778-8be51bf99bb1?q=80&w=2574&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        "https://images.unsplash.com/photo-1726715245558-69afa5ded798?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxmZWF0dXJlZC1waG90b3MtZmVlZHw4fHx8ZW58MHx8fHx8",
        "https://images.unsplash.com/photo-1726309356095-e4c9be366c13?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxmZWF0dXJlZC1waG90b3MtZmVlZHw5fHx8ZW58MHx8fHx8",
        "https://images.unsplash.com/photo-1726697187202-c1c33efd40d6?q=80&w=2669&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        "https://images.unsplash.com/photo-1726808260756-ec1d4eceaf71?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxmZWF0dXJlZC1waG90b3MtZmVlZHwyMHx8fGVufDB8fHx8fA%3D%3D",
        "https://images.unsplash.com/photo-1726758267577-f8ca9449ed6b?q=80&w=2574&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        "https://images.unsplash.com/photo-1721332155637-8b339526cf4c?q=80&w=2535&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDF8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        "https://images.unsplash.com/photo-1726503015583-0eafe04e0ded?q=80&w=2574&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    ],
    tags=['#randomTag', '#randomTag2'],
    # link_attachments=['https://pryxy.com','https://developers.facebook.com/docs/threads/posts#tags-and-links-in-posts', 'https://github.com/paulosabayomi'],
)

print("pipe", pipe)