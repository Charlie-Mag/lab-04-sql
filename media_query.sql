SELECT users.first_name, users.last_name, users.major, posts.title, posts.post_text
FROM users
JOIN posts
  WHERE users.user_id = posts.user_id
    AND users.major = 'Data Science';