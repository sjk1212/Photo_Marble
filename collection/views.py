from re import A
from django.shortcuts import render
from django.urls import reverse
from main.models import User, Collection, Landmark, Locations, Gallery

from django.db.models import Count

# Create your views here.


def collection_mypage(request):
    # progress bar
    ui = request.session['id']
    visited_landmark = Collection.objects.filter(user_id= ui)
    collection_cnt = len(visited_landmark)
    total = len(Landmark.objects.all())
    progress = int((collection_cnt/total)*100)

    # map
    area_id=[]
    for i in visited_landmark:
        l_d=i.landmark_id
        land=Landmark.objects.get(landmark_id= l_d)
        area_name=land.area
        land=Locations.objects.get(name= area_name)
        area_id.append('s'+str(land.location_id))

 
    data_list=[]
    for i in range(1,26):
        data_dict={}
        dict_key = 's'+str(i)
        if dict_key in area_id:

            data_dict['area']='area_true'
            data_dict['marker']='marker'
            data_list.append(data_dict)
        else:

            data_dict['area']='area_false'
            data_dict['marker']='empty'
            data_list.append(data_dict)
    # svg 태그 안에서 foor loop가 불가능해 우선은 하드코딩 (25개 개별로 전달) 추후에 수정 예정 ....
    # import json
    # a_list=json.dumps(area_list)
    test_dict={}
    for i in range(0, 25):
        print(data_list[0])
        test_dict['s{}'.format(i+1)]= data_list[i]
    
    test_dict['progress'] = progress
    print(test_dict)
    # test={'progress' : progress,
    #         's1': data_list[0],
    #         's2': data_list[1],
    #         's3': data_list[2],
    #         's4': data_list[3],
    #         's5': data_list[4],
    #         's6': data_list[5],
    #         's7': data_list[6],
    #         's8': data_list[7],
    #         's9': data_list[8],
    #         's10':data_list[9],
    #         's11':data_list[10],
    #         's12':data_list[11],
    #         's13':data_list[12],
    #         's14':data_list[13],
    #         's15':data_list[14],
    #         's16':data_list[15],
    #         's17':data_list[16], 
    #         's18':data_list[17], 
    #         's19':data_list[18], 
    #         's20':data_list[19], 
    #         's21':data_list[20], 
    #         's22':data_list[21], 
    #         's23':data_list[22], 
    #         's24':data_list[23], 
    #         's25':data_list[24]

    #         # 'area':area_list,
    #         # 'marker':marker_list
    #         }
    # print(test)
    return render(request, '../templates/collection/collection_mypage.html', context=test_dict)


from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def my_gallery(request):
    ui = request.session['id']
    print(ui)
    loc_id = request.POST.get('loc_id')
    print(loc_id)
    loc=Locations.objects.get(location_id = loc_id)
    loc_name=loc.name
    land=Landmark.objects.get(area = loc_name)
    land_id=land.landmark_id
    print(land_id)
    my_galleries = Gallery.objects.filter(user=ui, landmark_id=land_id)
    content = {"datas" : my_galleries}
    return render(request, "../templates/collection/my_gallery.html" , context= content)


def maps(request):
    return render(request, "../templates/collection/collection_mypage.html")

# def collection_ranking(request):
#     total = len(Landmark.objects.all())
#     rank = Collection.objects.values('user_id').annotate(dcount=Count('user_id'))
#     user_rank=[]
#     for i in rank:
#         tmp = [list(i.values())[0], list(i.values())[1]]
#         tmp_user = User.objects.get(id=list(i.values())[0]).username
#         user_rank.append([tmp_user,int((tmp[1]/total)*100)])

#     user_rank.sort(key=lambda x:x[1])

#     return render(request, '../templates/collection/collection_ranking.html',{'rank':user_rank})

def collection_ranking(request):
    
    rank = list(Collection.objects.values('user_id').annotate(dcount=Count('user_id')))
    rank = sorted(rank, key=lambda x:x['dcount'], reverse=True)
    rank_list = []
    if len(rank)<10:
        idx=len(rank)
    else:
        idx = 10
    for i in range(idx):
        user = User.objects.get(id=(rank[i]['user_id']))
       # user = User.objects.get(id=)
        tmp_dict={}
        tmp_dict['username'] = user.nickname
        tmp_dict['cnt'] = rank[i]['dcount']
        tmp_dict['profile_photo'] = user.profile_photo
        tmp_dict['rank'] = (i+1)
        tmp_dict['color'] = (i+1) %2 
        rank_list.append(tmp_dict)
    return render(request, '../templates/collection/collection_ranking.html',
                    {'first':rank_list[0], 'second':rank_list[1],'third':rank_list[2],'top4_7':rank_list[3:]})
