from app.main import main


def test_main_prints_application_name(capsys) -> None:
    main()

    captured = capsys.readouterr()
    assert "Helper Fisica" in captured.out

