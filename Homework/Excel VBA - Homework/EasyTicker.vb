Sub stockMacro()

Dim currentTicker As String
Dim tickerVolume As Double
Dim rowCount As Double
Dim tickerRow As Double


rowCount = Cells(Rows.Count, 1).End(xlUp).Row - 1
Cells(1, 9).Value = "Ticker"
Cells(1, 10).Value = "Total Stock Value"
tickerRow = 2
currentTicker = Cells(2, 1).Value

For i = 1 To rowCount
    If Cells(i + 1, 1).Value = currentTicker Then
        
        Cells(tickerRow, 9).Value = currentTicker
        Cells(tickerRow, 10).Value = tickerVolume + Cells(i + 1, 7).Value
        tickerVolume = Cells(tickerRow, 10).Value

        Else
        currentTicker = Cells(i + 1, 1).Value
        tickerRow = tickerRow + 1
        Cells(tickerRow, 9).Value = currentTicker
        
        tickerVolume = 0
        Cells(tickerRow, 10).Value = tickerVolume + Cells(i + 1, 7).Value
        tickerVolume = Cells(tickerRow, 10).Value

        End If
    Next i

End Sub
