from app.main import main


def test_main_starts_tkinter_application(monkeypatch) -> None:
    calls = []

    class FakeRoot:
        def mainloop(self) -> None:
            calls.append("mainloop")

    root = FakeRoot()
    monkeypatch.setattr("app.main.tk.Tk", lambda: root)
    monkeypatch.setattr("app.main.create_app", lambda received_root: calls.append(received_root))

    main()

    assert calls == [root, "mainloop"]
