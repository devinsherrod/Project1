import csv

class VotingBallots:
    """
    A class that handles all voting ballot functions and
    keeps track of voting ballot votes.
    """
    def __init__(self):
        self.used_ids = set()
        self.csv_file = 'Ballots.csv'
        self.setup_csv()

    def setup_csv(self):
        """
        Setting up the csv file if it does not exist.But if it does exist
        loads previous ID's
        """
        try:
            with open(self.csv_file, 'x', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Voter ID', 'Candidate'])
        except FileExistsError:
            with open(self.csv_file, 'r') as file:
                reader = csv.reader(file)
                next(reader)
                for row in reader:
                    if row and row[0] and not row[0].startswith("TOTAL:"):
                        self.used_ids.add(row[0])

    def validation_votes(self, voter_id, candidate):
        """
        Validation of the votes.
        :param voter_id:
        :param candidate:
        :returns: Things that will appear in the feedback box
        if the parameters for the voting are valid are invalid.
        """
        if not voter_id.isdigit() or len(voter_id) != 5:
            return 'ID must be 5 digits'
        if voter_id in self.used_ids:
            return 'Used ID. Please enter a unique ID'
        if not candidate:
            return 'Please select a candidate'

        with open(self.csv_file, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([voter_id, candidate])
        self.used_ids.add(voter_id)

        self.update_totals()
        return 'Vote Successful'

    def update_totals(self):
        """
        Updating the total votes for each candidate
        """
        votes = {'JANE': 0, 'JOHN': 0, 'BILL': 0}

        with open(self.csv_file, 'r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                if row and not row[0].startswith('TOTAL:'):
                    if row[1] in votes:
                        votes[row[1]] += 1

        with open(self.csv_file, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([])
            for name, vote in votes.items():
                writer.writerow([f'TOTAL: {name}', vote])

