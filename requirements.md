

## Functional Requirements

1. Login
2. Logout
3. Create New Account
4. Delete Account
5. [User home page]
6. [Update User Information]
7. [Post pictures/text]
8. [Like/Dislike posts]
9. [Delete posts]
10. [Follow Users]
11. [Display others' profiles]
12. [Search Users]

## Non-functional Requirements

1. Works on Google Chrome
2. Consistent font throughout site
3. Text length constraint of no more than 250 characters for posts
4. Using elements from bootstraps

## Use Cases

### 1. Update User Information (Nick)
- **Pre-condition:** 

  1. User has logged in
  2. User is in home page and drop down menu 

- **Trigger:** 

  1. User clicks on `Update Account`
 
- **Primary Sequence:**
  
  1. System will display two different text boxes for username and bio
  2. User is able to type in username text box to change user name
  3. User is able to type in bio text box to change bio
  4. User clicks on submit to update the user information
 
- **Primary Postconditions:** 
 
  1. The user's information will be updated and will show new information in user homepage.
 
- **Alternate Sequence:** 
  
  1. User does not click submit
  2. User leaves text box for username empty
  3. User leaves text box for bio empty
 
 
### 2. Like/Dislike posts (Nick)
- **Pre-condition:** 
 
  1. User has logged in
 
- **Trigger:** 
 
  1. User clicks `like` or `dislike` button
 
- **Primary Sequence:**
  
  1.  System displays post from any user at home page or user profile
  2.  User either selects like or dislike button
  3.  System displays the number of likes/dislikes on the post already
  4.  User can scroll to another post
 
- **Primary Postconditions:**  
 
  1. Users recently inputted like/dislike will increment one to the amount of total likes/dislikes.
 
- **Alternate Sequence:** 
  
  1. User clicks both `like` and `dislike`
  2. System displays error prompting to either like or dislike a post
  3. Post is no longer liked or disliked by user
 
 
### 3. Post pictures/text (Josh)
- **Pre-condition:** 
 
  1. User has logged in
 
- **Trigger:** 
 
  1. User clicks on `post` button 
 
- **Primary Sequence:** 
 
  1. Click new post button
  2. System opens a text box UI for user to write in
  3. User can add a photo to the post by clicking on attachment button
  4. User is able to post by pressing the ‘post’ button
 
- **Primary Postconditions:**
 
  1. Post is able to be viewed by other users
  2. Post is able to get likes or dislikes
 
- **Alternate Sequence:**
 
  1. Posting pictures that are not supported
  2. Text entry is too long 
  3. Shows the character count 
 
 
### 4. Delete posts (Josh)
- **Pre-condition:** 
 
  1. User has logged in
 
- **Trigger:** 
 
  1.User clicks delete post
 
- **Primary Sequence:**
 
  1. user must go to post that they want to delete
  2. User clicks delete option
  3. User confirms deletion
  4. Post is removed and deleted from db
 
- **Primary Postconditions:** 
 
  1. post will be removed, user will be redirected
 
- **Alternate Sequence:**
 
  1. User does not confirm deletion
  2. The user will be redirected
 
 
### 5. Search users (Jose C.)
- **pre-condition:**  
 
  1. User has logged in
  2. User is in homepage
 
- **Trigger:**
 
  1. User clicks on `search bar`
 
- **Primary-sequence:**
 
  1. User hovers over search bar
  2. User types username
  3. System prints suggestions
  4. User can either click from suggestions or finish typing desired user
  5.User clicks on desired user profile
  6.System displays desired users homepage
 
- **Primary-postconditions:** 
 
  1. Users are able to explore desired searched users' homepage, click on posts, click on followers, etc.
 
- **Alternative sequence:**
 
  1. User makes a typo
  2. System displays error message saying user does not exist
  3. User must retry search
 
 
### 6. Follow user (Haolin)
- **Pre-condition:**  
 
  1. The account needs to exist 
  2. The followee needs to be logged in 

- **Trigger:** 
 
  1. User clicks on the `follow` button on the other user's profile 

- **Primary Sequence:**
  
  1. User click on the profile they want to follow 
  2. Click on the follow button 
  3. User wait for the follow request recipient to accept or decline
  4. System change the follow button to “followed”
  5. If the user clock on followed button again, it unfollows them

- **Primary Postconditions:** 
 
  1. If the user gets accepted the followed user displays on the user’s followed list.
  2. If the user gets declined, it will not show up on their follow list

- **Alternate Sequence:** 
 
  1. The user try to follow an account that is deleted
  2. A pop up message, or on screen display showing the user you trying to follow does not exist

### 7. Display current/ others’ user profile (Haolin)
- **Pre-condition:** 
  
  1. The user needs to be logged in 

- **Trigger:** 
 
  1. To view the other profile, you either need to search for them 
  2. Or click on their profile on your follow list 
  3. Click on a button that bring you to your own profile

- **Primary Sequence:**
  
  1. The user has logged in 
  2. They seach for other user account names 
  3. Click on their profile, and that brings you to their profile 
  4. Click on your profile on the top right, and bring you to your own profile

- **Primary Postconditions:** 
 
  1. The current user’s page and or anothers’ page, will display their user name, maybe a profile picture, the people that you/they have followed, and the amount of followed and followers you or they have. 

- **Alternate Sequence:** 
  
  1. You try to view a profile of an account that has been deleted
  2. The page will just be labeled the user does not exist or has been deleted

