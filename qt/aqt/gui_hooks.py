# Copyright: Ankitects Pty Ltd and contributors
# License: GNU AGPL, version 3 or later; http://www.gnu.org/licenses/agpl.html

"""
See pylib/anki/hooks.py
"""

from __future__ import annotations

from typing import Any, Callable, Dict, List, Tuple

import anki
import aqt
from anki.cards import Card
from anki.hooks import runFilter, runHook
from aqt.qt import QMenu

# New hook/filter handling
##############################################################################
# The code in this section is automatically generated - any edits you make
# will be lost. To add new hooks, see ../tools/genhooks_gui.py
#
# @@AUTOGEN@@


class _AddCardsDidAddNoteHook:
    _hooks: List[Callable[["anki.notes.Note"], None]] = []

    def append(self, cb: Callable[["anki.notes.Note"], None]) -> None:
        """(note: anki.notes.Note)"""
        self._hooks.append(cb)

    def remove(self, cb: Callable[["anki.notes.Note"], None]) -> None:
        if cb in self._hooks:
            self._hooks.remove(cb)

    def __call__(self, note: anki.notes.Note) -> None:
        for hook in self._hooks:
            try:
                hook(note)
            except:
                # if the hook fails, remove it
                self._hooks.remove(hook)
                raise
        # legacy support
        runHook("AddCards.noteAdded", note)


add_cards_did_add_note = _AddCardsDidAddNoteHook()


class _AddCardsWillShowHistoryMenuHook:
    _hooks: List[Callable[["aqt.addcards.AddCards", QMenu], None]] = []

    def append(self, cb: Callable[["aqt.addcards.AddCards", QMenu], None]) -> None:
        """(addcards: aqt.addcards.AddCards, menu: QMenu)"""
        self._hooks.append(cb)

    def remove(self, cb: Callable[["aqt.addcards.AddCards", QMenu], None]) -> None:
        if cb in self._hooks:
            self._hooks.remove(cb)

    def __call__(self, addcards: aqt.addcards.AddCards, menu: QMenu) -> None:
        for hook in self._hooks:
            try:
                hook(addcards, menu)
            except:
                # if the hook fails, remove it
                self._hooks.remove(hook)
                raise
        # legacy support
        runHook("AddCards.onHistory", addcards, menu)


add_cards_will_show_history_menu = _AddCardsWillShowHistoryMenuHook()


class _AvPlayerDidBeginPlayingHook:
    _hooks: List[Callable[["aqt.sound.Player", "anki.sound.AVTag"], None]] = []

    def append(
        self, cb: Callable[["aqt.sound.Player", "anki.sound.AVTag"], None]
    ) -> None:
        """(player: aqt.sound.Player, tag: anki.sound.AVTag)"""
        self._hooks.append(cb)

    def remove(
        self, cb: Callable[["aqt.sound.Player", "anki.sound.AVTag"], None]
    ) -> None:
        if cb in self._hooks:
            self._hooks.remove(cb)

    def __call__(self, player: aqt.sound.Player, tag: anki.sound.AVTag) -> None:
        for hook in self._hooks:
            try:
                hook(player, tag)
            except:
                # if the hook fails, remove it
                self._hooks.remove(hook)
                raise


av_player_did_begin_playing = _AvPlayerDidBeginPlayingHook()


class _AvPlayerDidEndPlayingHook:
    _hooks: List[Callable[["aqt.sound.Player"], None]] = []

    def append(self, cb: Callable[["aqt.sound.Player"], None]) -> None:
        """(player: aqt.sound.Player)"""
        self._hooks.append(cb)

    def remove(self, cb: Callable[["aqt.sound.Player"], None]) -> None:
        if cb in self._hooks:
            self._hooks.remove(cb)

    def __call__(self, player: aqt.sound.Player) -> None:
        for hook in self._hooks:
            try:
                hook(player)
            except:
                # if the hook fails, remove it
                self._hooks.remove(hook)
                raise


av_player_did_end_playing = _AvPlayerDidEndPlayingHook()


class _AvPlayerWillPlayHook:
    _hooks: List[Callable[["anki.sound.AVTag"], None]] = []

    def append(self, cb: Callable[["anki.sound.AVTag"], None]) -> None:
        """(tag: anki.sound.AVTag)"""
        self._hooks.append(cb)

    def remove(self, cb: Callable[["anki.sound.AVTag"], None]) -> None:
        if cb in self._hooks:
            self._hooks.remove(cb)

    def __call__(self, tag: anki.sound.AVTag) -> None:
        for hook in self._hooks:
            try:
                hook(tag)
            except:
                # if the hook fails, remove it
                self._hooks.remove(hook)
                raise


av_player_will_play = _AvPlayerWillPlayHook()


class _BrowserDidChangeRowHook:
    _hooks: List[Callable[["aqt.browser.Browser"], None]] = []

    def append(self, cb: Callable[["aqt.browser.Browser"], None]) -> None:
        """(browser: aqt.browser.Browser)"""
        self._hooks.append(cb)

    def remove(self, cb: Callable[["aqt.browser.Browser"], None]) -> None:
        if cb in self._hooks:
            self._hooks.remove(cb)

    def __call__(self, browser: aqt.browser.Browser) -> None:
        for hook in self._hooks:
            try:
                hook(browser)
            except:
                # if the hook fails, remove it
                self._hooks.remove(hook)
                raise
        # legacy support
        runHook("browser.rowChanged", browser)


browser_did_change_row = _BrowserDidChangeRowHook()


class _BrowserMenusDidInitHook:
    _hooks: List[Callable[["aqt.browser.Browser"], None]] = []

    def append(self, cb: Callable[["aqt.browser.Browser"], None]) -> None:
        """(browser: aqt.browser.Browser)"""
        self._hooks.append(cb)

    def remove(self, cb: Callable[["aqt.browser.Browser"], None]) -> None:
        if cb in self._hooks:
            self._hooks.remove(cb)

    def __call__(self, browser: aqt.browser.Browser) -> None:
        for hook in self._hooks:
            try:
                hook(browser)
            except:
                # if the hook fails, remove it
                self._hooks.remove(hook)
                raise
        # legacy support
        runHook("browser.setupMenus", browser)


browser_menus_did_init = _BrowserMenusDidInitHook()


class _BrowserWillShowContextMenuHook:
    _hooks: List[Callable[["aqt.browser.Browser", QMenu], None]] = []

    def append(self, cb: Callable[["aqt.browser.Browser", QMenu], None]) -> None:
        """(browser: aqt.browser.Browser, menu: QMenu)"""
        self._hooks.append(cb)

    def remove(self, cb: Callable[["aqt.browser.Browser", QMenu], None]) -> None:
        if cb in self._hooks:
            self._hooks.remove(cb)

    def __call__(self, browser: aqt.browser.Browser, menu: QMenu) -> None:
        for hook in self._hooks:
            try:
                hook(browser, menu)
            except:
                # if the hook fails, remove it
                self._hooks.remove(hook)
                raise
        # legacy support
        runHook("browser.onContextMenu", browser, menu)


browser_will_show_context_menu = _BrowserWillShowContextMenuHook()


class _CardWillShowFilter:
    """Can modify card text before review/preview."""

    _hooks: List[Callable[[str, Card, str], str]] = []

    def append(self, cb: Callable[[str, Card, str], str]) -> None:
        """(text: str, card: Card, kind: str)"""
        self._hooks.append(cb)

    def remove(self, cb: Callable[[str, Card, str], str]) -> None:
        if cb in self._hooks:
            self._hooks.remove(cb)

    def __call__(self, text: str, card: Card, kind: str) -> str:
        for filter in self._hooks:
            try:
                text = filter(text, card, kind)
            except:
                # if the hook fails, remove it
                self._hooks.remove(filter)
                raise
        # legacy support
        runFilter("prepareQA", text, card, kind)
        return text


card_will_show = _CardWillShowFilter()


class _CollectionDidLoadHook:
    _hooks: List[Callable[["anki.storage._Collection"], None]] = []

    def append(self, cb: Callable[["anki.storage._Collection"], None]) -> None:
        """(col: anki.storage._Collection)"""
        self._hooks.append(cb)

    def remove(self, cb: Callable[["anki.storage._Collection"], None]) -> None:
        if cb in self._hooks:
            self._hooks.remove(cb)

    def __call__(self, col: anki.storage._Collection) -> None:
        for hook in self._hooks:
            try:
                hook(col)
            except:
                # if the hook fails, remove it
                self._hooks.remove(hook)
                raise
        # legacy support
        runHook("colLoading", col)


collection_did_load = _CollectionDidLoadHook()


class _CurrentNoteTypeDidChangeHook:
    _hooks: List[Callable[[Dict[str, Any]], None]] = []

    def append(self, cb: Callable[[Dict[str, Any]], None]) -> None:
        """(notetype: Dict[str, Any])"""
        self._hooks.append(cb)

    def remove(self, cb: Callable[[Dict[str, Any]], None]) -> None:
        if cb in self._hooks:
            self._hooks.remove(cb)

    def __call__(self, notetype: Dict[str, Any]) -> None:
        for hook in self._hooks:
            try:
                hook(notetype)
            except:
                # if the hook fails, remove it
                self._hooks.remove(hook)
                raise
        # legacy support
        runHook("currentModelChanged")


current_note_type_did_change = _CurrentNoteTypeDidChangeHook()


class _DeckBrowserWillShowOptionsMenuHook:
    _hooks: List[Callable[[QMenu, int], None]] = []

    def append(self, cb: Callable[[QMenu, int], None]) -> None:
        """(menu: QMenu, deck_id: int)"""
        self._hooks.append(cb)

    def remove(self, cb: Callable[[QMenu, int], None]) -> None:
        if cb in self._hooks:
            self._hooks.remove(cb)

    def __call__(self, menu: QMenu, deck_id: int) -> None:
        for hook in self._hooks:
            try:
                hook(menu, deck_id)
            except:
                # if the hook fails, remove it
                self._hooks.remove(hook)
                raise
        # legacy support
        runHook("showDeckOptions", menu, deck_id)


deck_browser_will_show_options_menu = _DeckBrowserWillShowOptionsMenuHook()


class _EditorDidFireTypingTimerHook:
    _hooks: List[Callable[["anki.notes.Note"], None]] = []

    def append(self, cb: Callable[["anki.notes.Note"], None]) -> None:
        """(note: anki.notes.Note)"""
        self._hooks.append(cb)

    def remove(self, cb: Callable[["anki.notes.Note"], None]) -> None:
        if cb in self._hooks:
            self._hooks.remove(cb)

    def __call__(self, note: anki.notes.Note) -> None:
        for hook in self._hooks:
            try:
                hook(note)
            except:
                # if the hook fails, remove it
                self._hooks.remove(hook)
                raise
        # legacy support
        runHook("editTimer", note)


editor_did_fire_typing_timer = _EditorDidFireTypingTimerHook()


class _EditorDidFocusFieldHook:
    _hooks: List[Callable[["anki.notes.Note", int], None]] = []

    def append(self, cb: Callable[["anki.notes.Note", int], None]) -> None:
        """(note: anki.notes.Note, current_field_idx: int)"""
        self._hooks.append(cb)

    def remove(self, cb: Callable[["anki.notes.Note", int], None]) -> None:
        if cb in self._hooks:
            self._hooks.remove(cb)

    def __call__(self, note: anki.notes.Note, current_field_idx: int) -> None:
        for hook in self._hooks:
            try:
                hook(note, current_field_idx)
            except:
                # if the hook fails, remove it
                self._hooks.remove(hook)
                raise
        # legacy support
        runHook("editFocusGained", note, current_field_idx)


editor_did_focus_field = _EditorDidFocusFieldHook()


class _EditorDidInitButtonsHook:
    _hooks: List[Callable[[List, "aqt.editor.Editor"], None]] = []

    def append(self, cb: Callable[[List, "aqt.editor.Editor"], None]) -> None:
        """(buttons: List, editor: aqt.editor.Editor)"""
        self._hooks.append(cb)

    def remove(self, cb: Callable[[List, "aqt.editor.Editor"], None]) -> None:
        if cb in self._hooks:
            self._hooks.remove(cb)

    def __call__(self, buttons: List, editor: aqt.editor.Editor) -> None:
        for hook in self._hooks:
            try:
                hook(buttons, editor)
            except:
                # if the hook fails, remove it
                self._hooks.remove(hook)
                raise


editor_did_init_buttons = _EditorDidInitButtonsHook()


class _EditorDidInitShortcutsHook:
    _hooks: List[Callable[[List[Tuple], "aqt.editor.Editor"], None]] = []

    def append(self, cb: Callable[[List[Tuple], "aqt.editor.Editor"], None]) -> None:
        """(shortcuts: List[Tuple], editor: aqt.editor.Editor)"""
        self._hooks.append(cb)

    def remove(self, cb: Callable[[List[Tuple], "aqt.editor.Editor"], None]) -> None:
        if cb in self._hooks:
            self._hooks.remove(cb)

    def __call__(self, shortcuts: List[Tuple], editor: aqt.editor.Editor) -> None:
        for hook in self._hooks:
            try:
                hook(shortcuts, editor)
            except:
                # if the hook fails, remove it
                self._hooks.remove(hook)
                raise
        # legacy support
        runHook("setupEditorShortcuts", shortcuts, editor)


editor_did_init_shortcuts = _EditorDidInitShortcutsHook()


class _EditorDidLoadNoteHook:
    _hooks: List[Callable[["aqt.editor.Editor"], None]] = []

    def append(self, cb: Callable[["aqt.editor.Editor"], None]) -> None:
        """(editor: aqt.editor.Editor)"""
        self._hooks.append(cb)

    def remove(self, cb: Callable[["aqt.editor.Editor"], None]) -> None:
        if cb in self._hooks:
            self._hooks.remove(cb)

    def __call__(self, editor: aqt.editor.Editor) -> None:
        for hook in self._hooks:
            try:
                hook(editor)
            except:
                # if the hook fails, remove it
                self._hooks.remove(hook)
                raise
        # legacy support
        runHook("loadNote", editor)


editor_did_load_note = _EditorDidLoadNoteHook()


class _EditorDidUnfocusFieldFilter:
    _hooks: List[Callable[[bool, "anki.notes.Note", int], bool]] = []

    def append(self, cb: Callable[[bool, "anki.notes.Note", int], bool]) -> None:
        """(changed: bool, note: anki.notes.Note, current_field_idx: int)"""
        self._hooks.append(cb)

    def remove(self, cb: Callable[[bool, "anki.notes.Note", int], bool]) -> None:
        if cb in self._hooks:
            self._hooks.remove(cb)

    def __call__(
        self, changed: bool, note: anki.notes.Note, current_field_idx: int
    ) -> bool:
        for filter in self._hooks:
            try:
                changed = filter(changed, note, current_field_idx)
            except:
                # if the hook fails, remove it
                self._hooks.remove(filter)
                raise
        # legacy support
        runFilter("editFocusLost", changed, note, current_field_idx)
        return changed


editor_did_unfocus_field = _EditorDidUnfocusFieldFilter()


class _EditorDidUpdateTagsHook:
    _hooks: List[Callable[["anki.notes.Note"], None]] = []

    def append(self, cb: Callable[["anki.notes.Note"], None]) -> None:
        """(note: anki.notes.Note)"""
        self._hooks.append(cb)

    def remove(self, cb: Callable[["anki.notes.Note"], None]) -> None:
        if cb in self._hooks:
            self._hooks.remove(cb)

    def __call__(self, note: anki.notes.Note) -> None:
        for hook in self._hooks:
            try:
                hook(note)
            except:
                # if the hook fails, remove it
                self._hooks.remove(hook)
                raise
        # legacy support
        runHook("tagsUpdated", note)


editor_did_update_tags = _EditorDidUpdateTagsHook()


class _EditorWillShowContextMenuHook:
    _hooks: List[Callable[["aqt.editor.EditorWebView", QMenu], None]] = []

    def append(self, cb: Callable[["aqt.editor.EditorWebView", QMenu], None]) -> None:
        """(editor_webview: aqt.editor.EditorWebView, menu: QMenu)"""
        self._hooks.append(cb)

    def remove(self, cb: Callable[["aqt.editor.EditorWebView", QMenu], None]) -> None:
        if cb in self._hooks:
            self._hooks.remove(cb)

    def __call__(self, editor_webview: aqt.editor.EditorWebView, menu: QMenu) -> None:
        for hook in self._hooks:
            try:
                hook(editor_webview, menu)
            except:
                # if the hook fails, remove it
                self._hooks.remove(hook)
                raise
        # legacy support
        runHook("EditorWebView.contextMenuEvent", editor_webview, menu)


editor_will_show_context_menu = _EditorWillShowContextMenuHook()


class _EditorWillUseFontForFieldFilter:
    _hooks: List[Callable[[str], str]] = []

    def append(self, cb: Callable[[str], str]) -> None:
        """(font: str)"""
        self._hooks.append(cb)

    def remove(self, cb: Callable[[str], str]) -> None:
        if cb in self._hooks:
            self._hooks.remove(cb)

    def __call__(self, font: str) -> str:
        for filter in self._hooks:
            try:
                font = filter(font)
            except:
                # if the hook fails, remove it
                self._hooks.remove(filter)
                raise
        # legacy support
        runFilter("mungeEditingFontName", font)
        return font


editor_will_use_font_for_field = _EditorWillUseFontForFieldFilter()


class _ProfileDidOpenHook:
    _hooks: List[Callable[[], None]] = []

    def append(self, cb: Callable[[], None]) -> None:
        """()"""
        self._hooks.append(cb)

    def remove(self, cb: Callable[[], None]) -> None:
        if cb in self._hooks:
            self._hooks.remove(cb)

    def __call__(self) -> None:
        for hook in self._hooks:
            try:
                hook()
            except:
                # if the hook fails, remove it
                self._hooks.remove(hook)
                raise
        # legacy support
        runHook("profileLoaded")


profile_did_open = _ProfileDidOpenHook()


class _ProfileWillCloseHook:
    _hooks: List[Callable[[], None]] = []

    def append(self, cb: Callable[[], None]) -> None:
        """()"""
        self._hooks.append(cb)

    def remove(self, cb: Callable[[], None]) -> None:
        if cb in self._hooks:
            self._hooks.remove(cb)

    def __call__(self) -> None:
        for hook in self._hooks:
            try:
                hook()
            except:
                # if the hook fails, remove it
                self._hooks.remove(hook)
                raise
        # legacy support
        runHook("unloadProfile")


profile_will_close = _ProfileWillCloseHook()


class _ReviewDidUndoHook:
    _hooks: List[Callable[[int], None]] = []

    def append(self, cb: Callable[[int], None]) -> None:
        """(card_id: int)"""
        self._hooks.append(cb)

    def remove(self, cb: Callable[[int], None]) -> None:
        if cb in self._hooks:
            self._hooks.remove(cb)

    def __call__(self, card_id: int) -> None:
        for hook in self._hooks:
            try:
                hook(card_id)
            except:
                # if the hook fails, remove it
                self._hooks.remove(hook)
                raise
        # legacy support
        runHook("revertedCard", card_id)


review_did_undo = _ReviewDidUndoHook()


class _ReviewerDidShowAnswerHook:
    _hooks: List[Callable[[Card], None]] = []

    def append(self, cb: Callable[[Card], None]) -> None:
        """(card: Card)"""
        self._hooks.append(cb)

    def remove(self, cb: Callable[[Card], None]) -> None:
        if cb in self._hooks:
            self._hooks.remove(cb)

    def __call__(self, card: Card) -> None:
        for hook in self._hooks:
            try:
                hook(card)
            except:
                # if the hook fails, remove it
                self._hooks.remove(hook)
                raise
        # legacy support
        runHook("showAnswer")


reviewer_did_show_answer = _ReviewerDidShowAnswerHook()


class _ReviewerDidShowQuestionHook:
    _hooks: List[Callable[[Card], None]] = []

    def append(self, cb: Callable[[Card], None]) -> None:
        """(card: Card)"""
        self._hooks.append(cb)

    def remove(self, cb: Callable[[Card], None]) -> None:
        if cb in self._hooks:
            self._hooks.remove(cb)

    def __call__(self, card: Card) -> None:
        for hook in self._hooks:
            try:
                hook(card)
            except:
                # if the hook fails, remove it
                self._hooks.remove(hook)
                raise
        # legacy support
        runHook("showQuestion")


reviewer_did_show_question = _ReviewerDidShowQuestionHook()


class _ReviewerWillEndHook:
    """Called before Anki transitions from the review screen to another screen."""

    _hooks: List[Callable[[], None]] = []

    def append(self, cb: Callable[[], None]) -> None:
        """()"""
        self._hooks.append(cb)

    def remove(self, cb: Callable[[], None]) -> None:
        if cb in self._hooks:
            self._hooks.remove(cb)

    def __call__(self) -> None:
        for hook in self._hooks:
            try:
                hook()
            except:
                # if the hook fails, remove it
                self._hooks.remove(hook)
                raise
        # legacy support
        runHook("reviewCleanup")


reviewer_will_end = _ReviewerWillEndHook()


class _ReviewerWillShowContextMenuHook:
    _hooks: List[Callable[["aqt.reviewer.Reviewer", QMenu], None]] = []

    def append(self, cb: Callable[["aqt.reviewer.Reviewer", QMenu], None]) -> None:
        """(reviewer: aqt.reviewer.Reviewer, menu: QMenu)"""
        self._hooks.append(cb)

    def remove(self, cb: Callable[["aqt.reviewer.Reviewer", QMenu], None]) -> None:
        if cb in self._hooks:
            self._hooks.remove(cb)

    def __call__(self, reviewer: aqt.reviewer.Reviewer, menu: QMenu) -> None:
        for hook in self._hooks:
            try:
                hook(reviewer, menu)
            except:
                # if the hook fails, remove it
                self._hooks.remove(hook)
                raise
        # legacy support
        runHook("Reviewer.contextMenuEvent", reviewer, menu)


reviewer_will_show_context_menu = _ReviewerWillShowContextMenuHook()


class _StateDidChangeHook:
    _hooks: List[Callable[[str, str], None]] = []

    def append(self, cb: Callable[[str, str], None]) -> None:
        """(new_state: str, old_state: str)"""
        self._hooks.append(cb)

    def remove(self, cb: Callable[[str, str], None]) -> None:
        if cb in self._hooks:
            self._hooks.remove(cb)

    def __call__(self, new_state: str, old_state: str) -> None:
        for hook in self._hooks:
            try:
                hook(new_state, old_state)
            except:
                # if the hook fails, remove it
                self._hooks.remove(hook)
                raise
        # legacy support
        runHook("afterStateChange", new_state, old_state)


state_did_change = _StateDidChangeHook()


class _StateDidResetHook:
    """Called when the interface needs to be redisplayed after non-trivial changes have been made."""

    _hooks: List[Callable[[], None]] = []

    def append(self, cb: Callable[[], None]) -> None:
        """()"""
        self._hooks.append(cb)

    def remove(self, cb: Callable[[], None]) -> None:
        if cb in self._hooks:
            self._hooks.remove(cb)

    def __call__(self) -> None:
        for hook in self._hooks:
            try:
                hook()
            except:
                # if the hook fails, remove it
                self._hooks.remove(hook)
                raise
        # legacy support
        runHook("reset")


state_did_reset = _StateDidResetHook()


class _StateDidRevertHook:
    """Called when user used the undo option to restore to an earlier database state."""

    _hooks: List[Callable[[str], None]] = []

    def append(self, cb: Callable[[str], None]) -> None:
        """(action: str)"""
        self._hooks.append(cb)

    def remove(self, cb: Callable[[str], None]) -> None:
        if cb in self._hooks:
            self._hooks.remove(cb)

    def __call__(self, action: str) -> None:
        for hook in self._hooks:
            try:
                hook(action)
            except:
                # if the hook fails, remove it
                self._hooks.remove(hook)
                raise
        # legacy support
        runHook("revertedState", action)


state_did_revert = _StateDidRevertHook()


class _StateShortcutsWillChangeHook:
    _hooks: List[Callable[[str, List[Tuple[str, Callable]]], None]] = []

    def append(self, cb: Callable[[str, List[Tuple[str, Callable]]], None]) -> None:
        """(state: str, shortcuts: List[Tuple[str, Callable]])"""
        self._hooks.append(cb)

    def remove(self, cb: Callable[[str, List[Tuple[str, Callable]]], None]) -> None:
        if cb in self._hooks:
            self._hooks.remove(cb)

    def __call__(self, state: str, shortcuts: List[Tuple[str, Callable]]) -> None:
        for hook in self._hooks:
            try:
                hook(state, shortcuts)
            except:
                # if the hook fails, remove it
                self._hooks.remove(hook)
                raise


state_shortcuts_will_change = _StateShortcutsWillChangeHook()


class _StateWillChangeHook:
    _hooks: List[Callable[[str, str], None]] = []

    def append(self, cb: Callable[[str, str], None]) -> None:
        """(new_state: str, old_state: str)"""
        self._hooks.append(cb)

    def remove(self, cb: Callable[[str, str], None]) -> None:
        if cb in self._hooks:
            self._hooks.remove(cb)

    def __call__(self, new_state: str, old_state: str) -> None:
        for hook in self._hooks:
            try:
                hook(new_state, old_state)
            except:
                # if the hook fails, remove it
                self._hooks.remove(hook)
                raise
        # legacy support
        runHook("beforeStateChange", new_state, old_state)


state_will_change = _StateWillChangeHook()


class _StyleDidInitFilter:
    _hooks: List[Callable[[str], str]] = []

    def append(self, cb: Callable[[str], str]) -> None:
        """(style: str)"""
        self._hooks.append(cb)

    def remove(self, cb: Callable[[str], str]) -> None:
        if cb in self._hooks:
            self._hooks.remove(cb)

    def __call__(self, style: str) -> str:
        for filter in self._hooks:
            try:
                style = filter(style)
            except:
                # if the hook fails, remove it
                self._hooks.remove(filter)
                raise
        # legacy support
        runFilter("setupStyle", style)
        return style


style_did_init = _StyleDidInitFilter()


class _UndoStateDidChangeHook:
    _hooks: List[Callable[[bool], None]] = []

    def append(self, cb: Callable[[bool], None]) -> None:
        """(can_undo: bool)"""
        self._hooks.append(cb)

    def remove(self, cb: Callable[[bool], None]) -> None:
        if cb in self._hooks:
            self._hooks.remove(cb)

    def __call__(self, can_undo: bool) -> None:
        for hook in self._hooks:
            try:
                hook(can_undo)
            except:
                # if the hook fails, remove it
                self._hooks.remove(hook)
                raise
        # legacy support
        runHook("undoState", can_undo)


undo_state_did_change = _UndoStateDidChangeHook()


class _WebviewDidReceiveJsMessageFilter:
    """Used to handle pycmd() messages sent from Javascript.
        
        Message is the string passed to pycmd(). Context is what was
        passed to set_bridge_command(), such as 'editor' or 'reviewer'.
        
        For messages you don't want to handle, return handled unchanged.
        
        If you handle a message and don't want it passed to the original
        bridge command handler, return (True, None).
          
        If you want to pass a value to pycmd's result callback, you can
        return it with (True, some_value)."""

    _hooks: List[Callable[[Tuple[bool, Any], str, str], Tuple[bool, Any]]] = []

    def append(
        self, cb: Callable[[Tuple[bool, Any], str, str], Tuple[bool, Any]]
    ) -> None:
        """(handled: Tuple[bool, Any], message: str, context: str)"""
        self._hooks.append(cb)

    def remove(
        self, cb: Callable[[Tuple[bool, Any], str, str], Tuple[bool, Any]]
    ) -> None:
        if cb in self._hooks:
            self._hooks.remove(cb)

    def __call__(
        self, handled: Tuple[bool, Any], message: str, context: str
    ) -> Tuple[bool, Any]:
        for filter in self._hooks:
            try:
                handled = filter(handled, message, context)
            except:
                # if the hook fails, remove it
                self._hooks.remove(filter)
                raise
        return handled


webview_did_receive_js_message = _WebviewDidReceiveJsMessageFilter()


class _WebviewWillShowContextMenuHook:
    _hooks: List[Callable[["aqt.webview.AnkiWebView", QMenu], None]] = []

    def append(self, cb: Callable[["aqt.webview.AnkiWebView", QMenu], None]) -> None:
        """(webview: aqt.webview.AnkiWebView, menu: QMenu)"""
        self._hooks.append(cb)

    def remove(self, cb: Callable[["aqt.webview.AnkiWebView", QMenu], None]) -> None:
        if cb in self._hooks:
            self._hooks.remove(cb)

    def __call__(self, webview: aqt.webview.AnkiWebView, menu: QMenu) -> None:
        for hook in self._hooks:
            try:
                hook(webview, menu)
            except:
                # if the hook fails, remove it
                self._hooks.remove(hook)
                raise
        # legacy support
        runHook("AnkiWebView.contextMenuEvent", webview, menu)


webview_will_show_context_menu = _WebviewWillShowContextMenuHook()
# @@AUTOGEN@@
