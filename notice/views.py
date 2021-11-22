from rest_framework import viewsets
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .serializers import Notice_PostSerializer , CommentSerializer

from django.contrib.auth.models import User
from .models import Notice_Post , Comment
from rest_framework.response import Response
from rest_framework.decorators import action
################## django api view ###################
from . import notice_prep
import os
from docx.shared import Cm
from docxtpl import DocxTemplate, InlineImage
from docx.shared import Cm, Inches, Mm, Emu
# import random
import datetime
from datetime import date
import aspose.words as aw



class Notice_PostViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Notice_Post.objects.all()
    serializer_class = Notice_PostSerializer
    filter_fields = (
        'is_assignment',
        'author',
    )


    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        if request.data['template_docx'] :
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

        else :
            author = request.user
            desig = request.data['desig']
            dept = request.data['department']
            Subject = request.data['subject']
            Date = datetime.datetime.now()
            content = request.data['content']
            template = DocxTemplate('media/Subject.docx')
            context = {
                'dept': dept,
                'date': Date,
                'Subject': Subject,
                'content': content,
                'desig': desig,
            }
            template.render(context)
            doc_name = "mdeia/" +str(author)+".docx"
            template.save('media/Subject1.docx')
            doc = aw.Document('media/Subject1.docx')
            doc.save("media/"+str(author)+".pdf")
            print("done")
            obj = Notice_Post.objects.latest('id')
            obj.template_docx =  os.path.abspath('media/notice.pdf')
            obj.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        
        

      

class CommentViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

            
        
    

    
    

