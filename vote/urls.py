from django.urls import path
from django.contrib import admin

from vote.views import users_views, votes_views

urlpatterns = [
    path("", users_views.index, name="index"),
    path("login",users_views.login_page, name="login"),
    path("signUp",users_views.signUp, name="signUp"),
    path("authenticateUser",users_views.authenticate_user,name="authenticateUser"), 
    path("createUser",users_views.create_user,name="createUser"),
    path("user/profile",users_views.login_user,name="user/profile"), 
    path("postBio/<str:username>",users_views.post_bio,name="postBio"),
    path("run_for_election/<str:username>",votes_views.run_for_election,name="run_for_election"),
    path("homePage",votes_views.home_page,name="homePage"),
    path("candidate/profile/<str:username>",votes_views.candidate_profile,name="candidate/profile"),  
    path("profile",users_views.profile,name="profile"),
    path("voteCandidate/<str:username>",votes_views.vote_candidate,name="voteCandidate") ,
    path("logout",users_views.logout_views,name="logout_views")      
]   
