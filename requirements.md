

# Functional Requirements

1. Login
2. Logout
3. Create New Account
4. Delete Account
5. [User home page](https://github.com/puibtx/131-Team10/blob/master/requirements.md#8-user-home-page-josh)
6. [Update User Information](https://github.com/puibtx/131-Team10/blob/master/requirements.md#1-update-user-information-nick)
7. [Post pictures/text](https://github.com/puibtx/131-Team10/blob/master/requirements.md#3-post-picturestext-josh)
8. [Upload Profile Picture](https://github.com/puibtx/131-Team10/blob/master/requirements.md#2-upload-profile-picture-nick)
9. [Delete posts](https://github.com/puibtx/131-Team10/blob/master/requirements.md#4-delete-posts-josh)
10. [Follow Users](https://github.com/puibtx/131-Team10/blob/master/requirements.md#6-follow-user-haolin)
11. [Display others' profiles](https://github.com/puibtx/131-Team10/blob/master/requirements.md#7-display-current-others-user-profile-haolin)
12. [Search Users](https://github.com/puibtx/131-Team10/blob/master/requirements.md#5-search-users-jose-c)

# Non-functional Requirements

1. Works on Google Chrome
2. Consistent font throughout site
3. Text length constraint of no more than 250 characters for posts
4. Using elements from bootstraps

# Use Cases

## 1. Update User Information (Nick)
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
 
 
## 2. Upload Profile Picture (Nick)
- **Pre-condition:** 
 
  1. User has logged in
 
- **Trigger:** 
 
  1. User clicks `Update Account` button
 
- **Primary Sequence:**
  
  1.  User clicks on the `User Settings` dropdown menu
  2.  Website will show three more buttons from the dropdown menu
  3.  User clicks on the `Update Account` button
  4.  User will be redirected to update account page
  5.  User can click on the `Choose File` button to pick a picture
  6.  User clicks on `Update Information` to upload the profile picture
 
- **Primary Postconditions:**  
 
  1. New profile picture will be displayed in the user home page
 
- **Alternate Sequence:** 
  
  1. User does not upload a picture
  2. User cannot upload certain files
 
 
## 3. Post pictures/text (Josh)
- **Pre-condition:** 
 
  1. User has logged in
 
- **Trigger:** 
 
  1. User clicks on `post` button 
 
- **Primary Sequence:** 
 
  1. Click new post button
  2. System opens a text box UI for user to write in
  3. User can add a photo to the post by clicking on the `Choose File` button
  5. User is able to post by pressing the ‘Add Post’ button
 
- **Primary Postconditions:**
 
  1. Post will be shown in user home page
  2. Post is able to be viewed by other users
  3. Post is able to get likes or dislikes
 
- **Alternate Sequence:**
 
  1. Posting pictures that are not supported
  2. Text entry is too long 
  3. Shows the character count 
 
 
## 4. Delete posts (Josh)
- **Pre-condition:** 
 
  1. User has logged in
 
- **Trigger:** 
 
  1. User clicks `Delete` button
 
- **Primary Sequence:**
 
  1. User is in the user home page and able to see all posts
  2. User user will click on the `Delete` button to delete their post
  4. Post is removed and deleted from db
 
- **Primary Postconditions:** 
 
  1. Post is removed and deleted from db
 
- **Alternate Sequence:**
 
  1. User wants to cancel the deletion
  2. User tries to get the file back
 
 
## 5. Search users (Jose C.)
- **pre-condition:**  
 
  1. User has logged in
  2. User is in homepage
 
- **Trigger:**
 
  1. User clicks on the `Search` button
 
- **Primary-sequence:**
 
  1. User clicks on the `Search` button
  2. User is redirected to the search page
  3. User can enter a known username into the text box
  4. User is able to click `Search` once they are done typine
 
- **Primary-postconditions:** 
 
  1. User is redirected to the searched user
 
- **Alternative sequence:**
 
  1. User makes a typo
  2. System displays error message saying user does not exist
  3. User must retry search
 
 
## 6. Follow user (Haolin)
- **Pre-condition:**  
 
  1. The account needs to exist 
  2. The follower needs to be logged in 

- **Trigger:** 
 
  1. User clicks on the `follow` button on the other user's profile 

- **Primary Sequence:**
  
  1. User click on the profile they want to follow 
  2. Click on the `follow` button 
  3. System change the follow button to “followed”
  4. If the user clock on followed button again, it unfollows them

- **Primary Postconditions:** 
 
  1. If the user gets accepted the followed user displays on the user’s followed list.
  2. If the user gets declined, it will not show up on their follow list

- **Alternate Sequence:** 
 
  1. The user try to follow an account that is deleted
  2. A pop up message, or on screen display showing the user you trying to follow does not exist

## 7. Display current/ others’ user profile (Haolin)

- **Pre-condition:** 
  
  1. The user needs to be logged in 

- **Trigger:** 
 
  1. To view the other profile, you either need to search for them 

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

## 8. User Home Page (Josh)
- **Pre-condition:** 
  
  1. The user needs to be logged in 

- **Trigger:** 
 
  1. User clicks on `Profile` button

- **Primary Sequence:**
  
  1. User will log into the webpage
  2. User will be redirected to the user home page after clicking `profile` button
  3. User is able to use the navbar at the top of the screen
  4. Buttons for the navbar will redirect user to what the buttons are titled

- **Primary Postconditions:** 
 
  1. System will show user information: Username, Follower and following count

- **Alternate Sequence:** 
  
  1. User clicks `home` button
  2. User does not log in and is unable to goto user home page



