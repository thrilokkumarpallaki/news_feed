# A News Feed

A console based flask application that can simulate a social network.

Users have the following capabilities (command to be used in [ - ]):

- [signup] A user can signup to the system
- [post] A user can post a feed item.
- [follow] Users can follow other users.
- [reply] A user can comment on another user's feed item.
- [upvote/downvote] Upvote or downvote posts.
- [newsfeed] Any user can read his news feed. News items are sorted based on the following (following options to sort feed by are available):
  
  - **Followed users:** posts by followed users appear first.

  - **Score (= upvotes - downvotes):** higher the better.
  - **The number of comments:** higher the better.
  - **Timestamp**: more recent the better. 

- Allow users to comment on a comment and upvote/downvote a comment.
- Display time in language like 2m ago, 1 hr ago etc.

## Input & output

### Signup Command
To register a new user, this signup command can be used.
> signup --name "Thrilok Kumar" --email thrilokkumarpallaki@gmail.com --password password

### login Command
To get the user information 
> login --email thrilokkumarpallaki@gmail.com --password password

### post Command
To create a feed item
> post --user 1 --content "Hey, How's it going!"

### Follow Command
To follow your favourite user
> follow --user 1 --follower 5

### Reply Command
To reply to a post
> reply --user 1 --feed 1 --comment "Going Good"

To reply to a comment
> reply --user 2 --feed 1 --comment "Hey, long time no see" --comment_id 1

### Upvote Feed Command
> upvote-feed --user 1 --feed 1

### Downvote Feed Command
> downvote-feed --user 1 --feed 1

### Upvote Comment Command
> upvote-comment --user 1 --comment 1

### Downvote Comment Command
> downvote-comment --user 1 --comment 1

### News Feed Command
> newsfeed --user 1