function getBlogPosts() {
    // Select the parent div (the one with class "w3-panel w3-border w3-padding-16 w3-mobile")
    const parentDiv = document.querySelector('div.w3-container.blog-container');

    // Get all direct child div elements
    const childDivs = Array.from(parentDiv.querySelectorAll(':scope > article'));

    return childDivs;
}

function reverseBlogPosts(postsArray) {
    // 1. Reverse the array of blog posts
    const reversedPosts = postsArray.reverse();

    // 2. Get the container element where posts are displayed
    const container = document.getElementById('posts');

    // 3. Clear the current content of the container
    container.innerHTML = '';

    // 4. Loop through the reversed array and append each post to the container
    reversedPosts.forEach(post => {
        container.appendChild(post);
  });
}

function reverseOnClick() {
    reverseBlogPosts(getBlogPosts());
}
