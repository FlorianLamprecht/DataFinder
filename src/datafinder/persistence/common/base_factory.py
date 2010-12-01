# pylint: disable=R0201, W0613
# $Filename$ 
# $Authors$
# Last Changed: $Date$ $Committer$ $Revision-Id$
#
# Copyright (c) 2003-2011, German Aerospace Center (DLR)
#
# All rights reserved.
#Redistribution and use in source and binary forms, with or without
#modification, are permitted provided that the following conditions are
#
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
Base class for the adaptor specific file system factory implementations.
"""


from datafinder.persistence.data.datastorer import NullDataStorer
from datafinder.persistence.metadata.metadatastorer import NullMetadataStorer
from datafinder.persistence.principal_search.principalsearcher import NullPrincipalSearcher
from datafinder.persistence.privileges.privilegestorer import NullPrivilegeStorer


__version__ = "$Revision-Id:$" 


class BaseFileSystem(object):
    """ Base class for the adaptor specific file system factory implementations. """
    
    def createDataStorer(self, identifier):
        """ 
        Factory method an adapter specific data storer. 
        
        @return: Adapter specific data storer.
        @rtype: instanceOf L{NullDataStorer<datafinder.persistence.data.datastorer.NullDataStorer>}
        """
        
        return NullDataStorer(identifier)
    
    def createMetadataStorer(self, identifier):
        """ 
        Factory method an adapter specific meta data storer. 
        
        @return: Adapter specific meta data storer.
        @rtype: instanceOf L{NullMetadataStorer<datafinder.persistence.metadata.metadatastorer.NullMetadataStorer>}
        """
        
        return NullMetadataStorer(identifier)
    
    def createPrivilegeStorer(self, identifier):
        """ 
        Factory method an adapter specific meta data storer. 
        
        @return: Adapter specific meta data storer.
        @rtype: instanceOf L{NullMetadataStorer<datafinder.persistence.privileges.privilegestorer.NullPrivilegeStorer>}
        """
        
        return NullPrivilegeStorer(identifier)
    
    def createPrincipalSearcher(self):
        """ 
        Factory method an adapter specific meta data storer. 
        
        @return: Adapter specific meta data storer.
        @rtype: instanceOf L{NullMetadataStorer<datafinder.persistence.privileges.privilegestorer.NullPrivilegeStorer>}
        """
        
        return NullPrincipalSearcher()

    def release(self):
        """ 
        @see: L{FileSystem.release<datafinder.persistence.factory.FileSystem.release>}
        @note: The default implementation does nothing.
        """
        
        pass

    def updateCredentials(self, credentials):
        """ 
        @see: L{FileSystem.updateCredentials<datafinder.persistence.factory.FileSystem.updateCredentials>} 
        @note: The default implementation does nothing.
        """
        
        pass

    def prepareUsage(self):
        """
        Prepares usage of the file system. 
        @note: The default implementation does nothing.
        """
    
        pass
    
    def isValidIdentifier(self, name): # W0613
        """ 
        @see: L{FileSystem.isValidIdentifier<datafinder.persistence.factory.FileSystem.metadataIdentifierPattern>}
        @note: This implementation always returns C{True}, C{None}.
        """
        
        return True, None

    def isValidMetadataIdentifier(self, name): # W0613
        """ 
        @see: L{FileSystem.metadataIdentifier<datafinder.persistence.factory.FileSystem.metadataIdentifierPattern>}
        @note: This implementation always returns C{True}, C{None}.
        """
        
        return True, None
    
    @property
    def hasCustomMetadataSupport(self):
        """ 
        @see: L{FileSystem.hasCustomMetadataSupport<datafinder.persistence.factory.FileSystem.hasCustomMetadataSupport>}
        @note: This implementation always returns C{False}.
        """
        
        return False
    
    @property
    def hasMetadataSearchSupport(self):
        """ 
        @see: L{FileSystem.hasMetadataSearchSupport<datafinder.persistence.factory.FileSystem.hasMetadataSearchSupport>}
        @note: This implementation always returns C{False}.
        """
        
        return False
    
    @property
    def hasPrivilegeSupport(self):
        """ 
        @see: L{FileSystem.hasPrivilegeSupport<datafinder.persistence.factory.FileSystem.hasPrivilegeSupport>}
        @note: This implementation always returns C{False}.
        """
    
        return False
