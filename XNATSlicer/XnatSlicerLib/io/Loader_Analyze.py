# external
from MokaUtils import *

# module
from SlicerUtils import *
from XnatSlicerUtils import *
from Loader import *




class Loader_Analyze(Loader_Images):
    """ 
    Class description above.  Inherits from Loader_Images.
    Loader_Analyze contains the specific load methods for analyze 
    filetypes (.hdr and .img pairings) to be downloaded from an XNAT host into Slicer.  
    """

    

    def __init__(self, MODULE, _src, fileUris):
        super(Loader_Analyze, self).__init__(MODULE, _src, fileUris)

    
        
        if self.useCached:
            # Update the download popup
            self._dst = None
            popupKey = self._src.replace('?format=zip', '')
            self.MODULE.LoadWorkflow.XnatDownloadPopup.setText(popupKey, 
                                                  "USING CACHED<br>'%s'"%(self.MODULE.LoadWorkflow.XnatDownloadPopup.makeDownloadPath(popupKey)))
            self.MODULE.LoadWorkflow.XnatDownloadPopup.setProgressBarValue(popupKey, 100)
            self.MODULE.LoadWorkflow.XnatDownloadPopup.setEnabled(popupKey, False)

            
            self.extractedFiles = self.cachedFiles
                                                                    
    

        
    def checkCache(self, *args):
        """
        """
        splitter = '/projects/'
     
        abbreviatedUris = [self._src.split(splitter)[1].replace('?format=zip', '') + '/' + os.path.basename(fileUri) for fileUri in self.fileUris]
        #print "ABBREVIATED URIS", abbreviatedUris
        
        foundCount = 0
        self.cachedFiles = []
        for root, dirs, files in os.walk(self._dst.replace('.zip', '')):
            for f in files:
                if XnatSlicerUtils.isAnalyze(f):
                    #print "\n\nCACHED ANALYZE", os.path.join(root, f), "\n\n", root, f
                    uri = os.path.join(root, f)
                    #print uri.split(splitter)[1] in abbreviatedUris
                    if uri.split(splitter)[1] in abbreviatedUris:
                        foundCount +=1
                        self.cachedFiles.append(uri)

        #print "FOUND", foundCount, "URS", len(abbreviatedUris)
        
        if foundCount == len(abbreviatedUris):
            return True

            
        
    def load(self):
        """ Downloads an analyze file pair (.hdr and .img) from XNAT, 
            then attempts to load it via the Slicer API's 'loadNodeFromFile' 
            method, which returns True or False if the load was successful.
        """

        if self.useCached:
            MokaUtils.debug.lf( "\n\nUsing cached analyze files:", self.extractedFiles, "\n\n")
            
            
        else:
            if not os.path.exists(self._dst): return 
            self.extractDst()
            
        for fileName in self.extractedFiles:
            SlicerUtils.loadNodeFromFile(fileName)



