# Instagram Database & Weekly Notification Subsystem

## 1. Project Background

### Udemy Code-Along
We kicked off with a standard Instagram schema built alongside a Udemy database course[cite: 1]:
* Tables for core social features: `users`, `posts`, `comments`, `likes`, `followers`, `hashtags`, `hashtags_posts`, `caption_tags`, and `photo_tags`[cite: 2].
* Covered basic app behaviors like liking either a post or a comment, tagging users on photos with X/Y coordinates, and following accounts[cite: 2].

<img width="940" height="574" alt="image" src="https://github.com/user-attachments/assets/fee55121-7101-4815-9f64-446f0b2a0397" />


---

### What Was Added (The Notification Extension)
* **Notifications:** Shows who liked your photo, dropped a comment, followed you, or tagged you[cite: 3].
* **Weekly email digest:** Bundles up your notifications from the last 7 days and sends one clean summary email with total counts[cite: 3].


<img width="876" height="658" alt="image" src="https://github.com/user-attachments/assets/ba5e55a3-73c2-43b0-90c9-3136db436b53" />


---

## 2. Table Breakdown
### Notification Tables
* **`notifications`:** The running list of every alert[cite: 3].
  * `actor_id` (who did it) and `recipient_id` (who gets notified)[cite: 3].
  * `type`: Plain text telling us what happened (`like_post`, `comment`, `follow`, etc.)[cite: 3].
  * `post_id` / `comment_id`: Optional links to the post or comment involved[cite: 3].
  * `digest_id`: Links to the email table once this alert has been bundled into a weekly email[cite: 3].
* **`email_digests`:** A log of every weekly email sent[cite: 3].
  * Stores the user, the time, and whether it sent or failed[cite: 3].
  * `attempts` & `last_error`: If an email fails to send, it notes how many times we retried and what went wrong[cite: 3].
  * Saved counts (`like_count`, `comment_count`, etc.): Keeps a permanent record of what numbers were sent in that email[cite: 3].

---

## 3. How the Tables Connect

* **`users` $\rightarrow$ `notifications`:** Every notification connects two users: the one who did the action and the one receiving it[cite: 3].
* **`posts` / `comments` $\rightarrow$ `notifications`:** If someone likes your post, the notification points to that post[cite: 3]. If someone follows you, both post and comment links stay empty[cite: 3].
* **`email_digests` $\rightarrow$ `notifications`:** When a weekly email goes out, all the notifications included in it get stamped with that email's `digest_id`[cite: 3]. That way, they are never emailed twice[cite: 3].

---

## 4. Key Design Decisions

### 1. Using a Single SQL Query to Count and Save (CTE)
When the weekly email job runs, we don't want to calculate counts in one query, insert into the email table in a second query, and update the notifications in a third. 

We bundle it all into one SQL query using a Common Table Expression (CTE). It counts the unbatched notifications, creates the `email_digests` record, and stamps the `digest_id` onto the notifications all in one clean step. This prevents race conditions where an email gets sent twice.

### 2. Clear `type` Names
Instead of trying to guess what happened based on which columns have values, we just write it out: `type = 'like_post'`, `type = 'follow'`, etc[cite: 3]. This makes it super straightforward for the front-end to show the right text and icon (like a heart icon for likes or a person icon for follows).

### 3. Storing the Final Email Numbers
We save the actual numbers (`like_count: 5`, `comment_count: 2`) directly in `email_digests`[cite: 3]. If a post or account gets deleted three weeks later, our email log still shows the exact numbers that landed in the user's inbox[cite: 3].

---

## 5. Indexes (Keeping Queries Fast)

* **`idx_notif_inbox (recipient_id, created_at)`:** Makes loading a user's notification feed fast and automatically sorted with the newest stuff on top.
* **`idx_notif_pending_digest (recipient_id, digest_id)`:** Helps the weekly email worker instantly find only the notifications that haven't been emailed yet (`digest_id IS NULL`), without scanning millions of old rows.
* **`idx_digests_user (user_id, created_at)`:** Makes it quick to check when a user last got a digest so we know who is due for their next one.
