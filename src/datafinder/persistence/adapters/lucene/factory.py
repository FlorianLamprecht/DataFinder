# $Filename$ 
# $Authors$
# Last Changed: $Date$ $Committer$ $Revision-Id$
#
# Copyright (c) 2003-2011, German Aerospace Center (DLR)
# All rights reserved.
#
#
#Redistribution and use in source and binary forms, with or without
#modification, are permitted provided that the following conditions are
#met:
#
# * Redistributions of source code must retain the above copyright 
#   notice, this list of conditions and the following disclaimer. 
#
# * Redistributions in binary form must reproduce the above copyright 
#   notice, this list of conditions and the following disclaimer in the 
#   documentation and/or other materials provided with the 
#   distribution. 
#
# * Neither the name of the German Aerospace Center nor the names of
#   its contributors may be used to endorse or promote products derived
#   from this software without specific prior written permission.
#
#THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS 
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT 
#LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR 
#A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT 
#OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, 
#SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT 
#LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, 
#DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY 
#THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT 
#(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE 
#OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.  


""" 
Lucene-specific factory implementation.
"""


import lucene

from datafinder.persistence.adapters.lucene.configuration import Configuration
from datafinder.persistence.adapters.lucene.search.adapter import SearchLuceneAdapter
from datafinder.persistence.common.base_factory import BaseFileSystem


__version__ = "$Revision-Id:$" 


class FileSystem(BaseFileSystem):
    """ Implements factory method of the different aspects of file system items. """
     
    def __init__(self, baseConfiguration):
        """ 
        @param baseConfiguration: General basic configuration.
        @type baseConfiguration: L{BaseConfiguration<datafinder.persistence.common.configuration.BaseConfiguration>}
        """
        # pylint can not recognize initVM method: pylint: disable=E1101
        
        BaseFileSystem.__init__(self)
        self._env = lucene.initVM()
        self._configuration = Configuration(baseConfiguration, self._env)
            
    def createSearcher(self):
        """ Factory method for the search object. """

        return SearchLuceneAdapter(self._configuration)

    @property
    def hasMetadataSearchSupport(self):
        """ @see: L{<BaseFileSystem.hasMetadataSearchSupport>datafinder.persistence.
        common.base_factory.BaseFileSystem.hasMetadataSearchSupport} """
        
        return True
