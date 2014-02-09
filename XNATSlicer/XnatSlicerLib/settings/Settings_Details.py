# python
from collections import OrderedDict

# external
from Xnat import *

# module
from Settings import *
from FontSetting import *
from MetadataEditorSetting import *
from CheckBoxSetting import *


    
class Settings_Details(FontSetting, MetadataEditorSetting, CheckBoxSetting, 
                       Settings):
    """ 
    Settings_Details is the Settings pertaining to the 'NodeDetails' class. 
    """

    LABEL_FONT_SIZE = 'Details Font Size' 
    LABEL_METADATA = 'Details Metadata' 
    CHECKBOXES = OrderedDict([
        ('empty', {
            'tag': 'showEmptyMetadata',
            'desc': 'Display metadata with empty values.',
            'checked': True,
            'event': 'SHOWEMPTY'
        })
    ])



    def setup(self):
        """
        Method inherited from parent function.
        """
        self.createCheckBoxes()
        self.addSpacing()
        self.addSpacing()
        self.createFontSizeDropdown(self.LABEL_FONT_SIZE)
        self.addSpacing()
        self.createMetadataEditorSets(self.LABEL_METADATA, 
                                      itemType = 'checkbox', 
                                      editVisible = True,
                                      customEditVisible = False) 








        
