"""
Game의 Manager 및 Interface를 포함

작성자: 김종하
"""

from abc import *

from enum import Enum
from discord import CategoryChannel
from discord import TextChannel
import random
import string

class GameType(Enum):
    NONE = 0
    GOMOKU = 1

class GameState(Enum):
    Wating = 0
    Proceeding = 1
    Paused = 2
    Ended = 3

class Game(metaclass=ABCMeta):
    """
    개별 게임 객체
    반드시 :class:`GameManager`를 통해 관리할 것

    Constructor Arguments
    ----------
    gameID[:class:`string`]: 게임의 ID
    
    gameType[:class:`GameType`]: 게임 종류
    """  
    __gameType = GameType.NONE    # Type: GameType
    __players = []                # Type: list[ClientUser]
    __gameRecord = ""
    __channel = TextChannel()

    # game
    def __init__(self, gameID, gameType):   
        """
        :class:`Game` Constructor

        Arguments
        ----------
        gameID[:class:`string`]: 게임의 ID
        
        gameType[:class:`GameType`]: 게임 종류
        """  
        return

    def registerPlayer(self, player):
        """
        참가자 등록

        Arguments
        ----------
        player[:class:`ClientUser`]: 등록할 유저 객체
        """
        self.__players.append(player)
        return

    def unregisterPlayer(self, player):
        """
        참가자 등록 해제

        Arguments
        ----------
        player[:class:`ClientUser`]: 등록 해제할 유저 객체
        """
        self.__players.remove(player)
        return

    def setGameState(self, gameState):
        """
        게임의 진행 상태 설정

        Arguments
        ----------
        gameState[:class:`GameState`]: 설정할 게임 상태
        """
        return

    # private methods
    
    def __createChannelForGame(self):
        """
        게임 진행용 TextChannel 생성 및 반환
    
        Returns
        --------
        생성한 :class:`TextChannel` 객체
        """
        return 

    def __deleteChannelForGame(self):
        """
        게임 진행용 TextChannel 삭제
        """
        return 

    # gets
    @property
    def channel(self):
        return self.__channel


class GameManager:
    '''
    게임 및 게임 ID의 생성, 삭제 등을 담당하는 클래스입니다.
    '''
    __gameIDLength = 8
    __games = {}
    __gameChannels = {}
    __errorGameObject = Game("ERROR", GameType.NONE)

    # Public Methods

    def registerManagerChannel(self, category):
        """
        GemeManager 사용을 위한 명령어 입력용 채널 등록

        Arguments
        ----------
        category[:class:``]: 게임의 종류
        """
        return

    def registerGameCategory(self, category):
        """
        게임 진행용 :class:`TextChannel`들을 관리하기 위한
        :class:`CategoryChannel` 생성

        Arguments
        ----------
        category[:class:``]: 게임의 종류
        """
        return

    def addGame(self, gameType):
        """
        매개받은 :class:`GameType`에 맞는 게임을 생성

        Arguments
        ----------
        gameType[:class:`GameType`]: 게임의 종류

        Returns
        --------
        생성한 :class:`Game` 객체의 ID[:class:`string`]
        """
        return

    def removeGame(self, gameID):
        """
        Game의 ID를 사용해서 해당 게임 삭제

        Arguments
        ----------
        gameID[:class:`string`]: 게임의 ID
        """
        return

    def startGame(self, gameID):
        """
        Game의 ID를 사용해서 해당 게임 시작

        Arguments
        ----------
        gameID[:class:`string`]: 게임의 ID
        """
        return

    def endGame(self, gameID):
        """
        Game의 ID를 사용해서 해당 게임 종료

        Arguments
        ----------
        gameID[:class:`string`]: 게임의 ID
        """
        return

    def getGameByID(self, gameID):
        """
        Game의 ID를 사용해서 해당 게임 조회

        Arguments
        ----------
        gameID[:class:`string`]: 게임의 ID
    
        Returns
        --------
        gameID에 해당하는 :class:`Game` 객체
        """
        return self.__games[gameID]

    # Private Methods

    def __createGameID(self):
        """
        Game의 ID 생성 및 반환

        Returns
        --------
        무작위로 생성된 Game의 ID 반환
        """
        gameIDLetterPool = string.ascii_letters
        gameID = ""
        for i in range(self.__gameIDLength):
            gameID += random.choice(gameIDLetterPool)
        return gameID