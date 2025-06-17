from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import DisasterEvent
from .serializers import DisasterEventSerializer

# Dummy AI functions (replace with real API calls as needed)
def analyze_satellite_image(image_path):
    # Simulate AI analysis
    return {"flooded_area": 0.5, "burn_severity": 0.2}

def summarize_text(text):
    # Simulate AI summarization
    return "AI-generated summary."

class DisasterEventListCreateView(generics.ListCreateAPIView):
    queryset = DisasterEvent.objects.all()
    serializer_class = DisasterEventSerializer

class DisasterEventDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DisasterEvent.objects.all()
    serializer_class = DisasterEventSerializer

class SatelliteImageUploadView(APIView):
    def post(self, request):
        image = request.FILES.get('image')
        if not image:
            return Response({"error": "No image uploaded"}, status=400)
        path = f"/tmp/{image.name}"
        with open(path, "wb") as f:
            for chunk in image.chunks():
                f.write(chunk)
        features = analyze_satellite_image(path)
        return Response(features)

class TextSummarizeView(APIView):
    def post(self, request):
        text = request.data.get("text")
        if not text:
            return Response({"error": "No text provided"}, status=400)
        summary = summarize_text(text)
        return Response({"summary": summary})

class DisasterEventSearchView(APIView):
    def get(self, request):
        dtype = request.GET.get("type")
        min_severity = float(request.GET.get("min_severity", 0))
        queryset = DisasterEvent.objects.all()
        if dtype:
            queryset = queryset.filter(disaster_type=dtype)
        if min_severity:
            queryset = queryset.filter(severity__gte=min_severity)
        serializer = DisasterEventSerializer(queryset, many=True)
        return Response(serializer.data)