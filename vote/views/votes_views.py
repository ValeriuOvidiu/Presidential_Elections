from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from vote.models import candidates, votes_candidate
from django.db.models import Count

def run_for_election(request,username):
      user=request.user
      if hasattr(user, "candidates"):
           candidate=candidates.objects.get(candidate=user)
           candidate.delete()
      else :
           candidate=candidates(candidate=user)
           candidate.save()
      return redirect("profile") 

def home_page(request):
     top_list=candidates.objects.annotate(num_votes=Count("votes_candidate")).order_by("-num_votes")[:5]
     context={
          "candidates_list":candidates.objects.all(),
          "top_list":top_list

     }
     return render(request,"vote/homePage.html",context) 

def candidate_profile(request, username):
     user=User.objects.get(username=username)
     bio="Empty bio"
     if hasattr(user, "profile"):
         bio=user.profile
     votes=votes_candidate.objects.filter(candidate=user.candidates).count()
     vote_or_change_vote="Vote " + user.first_name
     if hasattr(request.user,"votes_candidate"):
        vote_or_change_vote="Change your vote"
        
     context={
          "user":user,
          "bio":bio,
          'votes': votes,
          "vote_or_change_vote":vote_or_change_vote
     }

     return render(request, "vote/candidateProfile.html",context)  

def vote_candidate(request,username):
      user_candidate=User.objects.get(username=username)
      candidate=candidates.objects.get(candidate=user_candidate)
      voter=request.user 
      if hasattr (voter,"votes_candidate"):
           vote=votes_candidate.objects.get(voter=voter)
           vote.delete()
      else :  
        vote=votes_candidate(voter=voter,candidate=candidate)
        vote.save()   
      return redirect("candidate/profile",username) 
